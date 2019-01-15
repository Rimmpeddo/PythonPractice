class Update_list:
    def __init__(self, list):
        self.list = list

    def add_key(self, keyname):
        if isinstance(keyname, (int, str)):
            self.list.append(keyname)
            return self.list
        else:
            return "输入字符型或整数型"

    def get_key(self, index):
        if index < 0 and index >= len(self.list):
            return self.list[index]
        else:
            return "超出范围"

    def up_lt(self,list2):
        self.list.extend(list2)
        return self.list

    def del_key(self):
        if len(self.list) > 0:
            return self.list.pop(-1)
        else:
            return "没有可删除的元素"


class DictClass:
    def __init__(self, dict):
        self.dict = dict

    def del_key(self, key):
        if key in self.dict.keys():
            return self.dict.pop(key)
        else:
            return "不在字典中"

    def get_key(self, key):
        if key in self.dict.keys():
            return self.dict[key]
        else:
            return "Not found"

    def get_list_key(self):
        return self.dict.keys()

    def update_list(self, dict2):
        self.dict = dict(self.dict, **dict2)
        return self.dict


class Setinfo:
    def __init__(self, setinfo):
        self.setinfo = setinfo

    def add_set(self, info):
        self.setinfo.add(info)
        return self.setinfo

    def get_intersction(self, unionifo):
        return self.setinfo & unionifo

    def get_union(self, unioninfo):
        return self.setinfo | unioninfo

    def get_difference(self, unioninfo):
        return self.setinfo - unioninfo


