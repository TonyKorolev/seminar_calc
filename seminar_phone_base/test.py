import ui_test as ui
import logger
import assigment_id as id

entry_user = ui.get_user_info()
entry_user = id.assign_id(entry_user)
logger.log_json(entry_user)
logger.log_xml(entry_user)
