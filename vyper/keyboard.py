import json
import xlsxwriter
from xlrd import open_workbook
import itertools

class Keyboard:
	keyboard = {'inline_keyboard': []}
	def __init__(self, rows=1, columns=1):
		self.keyboard['inline_keyboard'] = [[{'text': 'Sample Text'} for col in range(columns)] for row in range(rows)]

	def write_to_excel(self, file):
		raise FutureWarning('The write_to_excel() method will be implemented in a future update.')

	def load_from_excel(self, file, click_type='callback_data', default_click='default_blank_callback'):
		buttons = []
		wb = open_workbook(file, formatting_info=True)
		sheet = wb.sheet_by_name("Sheet1")
		print('Reading keyboard from:', file)
		for col in range(sheet.ncols):
			text = data = ''
			buttons.append([])
			for row in range(sheet.nrows):
				cell = sheet.cell(row, col)
				fmt = wb.xf_list[cell.xf_index]
				border = fmt.border
				has_bottom = bool(border.bottom_line_style)
				if not has_bottom:
					text = str(cell.value)
				else:
					data = str(cell.value)
					if data and text:
						buttons[col].append({'text': text, click_type: data})
					else:
						buttons[col].append({'text': data, click_type: default_click})
					text = ''
					data = ''

			if not has_bottom and text:
				raise ExcelNoBottomException('Cell({0},{1}) has no bottom border.'.format(row, col))
			
		# Flip columns and rows
		buttons = list(map(list, itertools.zip_longest(*buttons)))
		buttons = [[button for button in row if button is not None] for row in buttons]
		self.keyboard['inline_keyboard'] = buttons
	@property
	def json(self):
		return json.dumps(self.keyboard)

class ExcelNoBottomException(BaseException):
	def __init__(self, message='There\'s no bottom border for one of your buttons.'):
		self.message = message