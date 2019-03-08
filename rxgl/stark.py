from stark.service.v1 import StarkHandler,site,Option,get_choice_text
from rxgl import models


class czcConfig(StarkHandler):
    list_display = [StarkHandler.display_checkbox,'gdbh','slsj','sllx','slnr','czlx','zbdw',StarkHandler.display_edit,StarkHandler.display_del]
    action_list = [StarkHandler.action_multi_delete]
    search_list = ['gdbh','sllx','zbdw']

site.register(models.czc,czcConfig)

class gjcConfig(StarkHandler):
    list_display = [StarkHandler.display_checkbox,'gdbh','slsj','sllx','slnr','zbdw',StarkHandler.display_edit,StarkHandler.display_del]
    action_list = [StarkHandler.action_multi_delete]
    search_list = ['gdbh','sllx','zbdw']

site.register(models.gjc,gjcConfig)

class taxiConfig(StarkHandler):
    list_display = [StarkHandler.display_checkbox,'gdbh','sfrq',get_choice_text("公司名称",'company'),'slnr','sqlb','czlx',StarkHandler.display_edit,StarkHandler.display_del]
    action_list = [StarkHandler.action_multi_delete]
    search_list = ['gdbh','sqlb']
    search_group = [
            # Option('czlx', is_multi=True),
            Option('sqlb', db_condition={'id__gt': 0},is_multi=True),
            Option('company', db_condition={'id__gt': 0},is_multi=True)
        ]

site.register(models.taxi,taxiConfig)


class busConfig(StarkHandler):
    list_display = [StarkHandler.display_checkbox,'gdbh','tsrq',"lb","bus_number",'slnr',get_choice_text("诉求类别",'sqlb'),'wait_time',"geton_address","getoff_address",StarkHandler.display_edit,StarkHandler.display_del]
    action_list = [StarkHandler.action_multi_delete]
    search_list = ['gdbh','sqlb']
    search_group = [
            # Option('czlx', is_multi=True),
            Option('sqlb', db_condition={'id__gt': 0},is_multi=True),
            # Option('company', db_condition={'id__gt': 0},is_multi=True)
        ]

site.register(models.bus,busConfig)