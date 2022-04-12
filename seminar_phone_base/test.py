import ui_test as ui
import logger


entry_user = ui.get_user_info()
logger.log_json(entry_user)
logger.log_xml(entry_user)
