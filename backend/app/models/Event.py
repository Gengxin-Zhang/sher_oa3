from app import db
from app.models.User import User
import datetime

class Event(db.Document):
    """
    这里是课表中一个格子展示的事件,模仿教务系统\n
    frequency：几周展示一次，比如两周一次的课程需要这个\n
    offset：对应frequency，是偏移，用来设置例如单双周的课程切换\n
        比如单周上英语，双周上数学的话,
        两者frequency都为2，offset分别为0,1\n
    start：从第几周开始展示\n
    end：到第几周停止展示\n
    timenode：0~34整数，表示当前事件位于哪个时间区间\n
    """
    user = db.ReferenceField(User,reverse_delete_rule=2)
    name = db.StringField()
    frequency = db.IntField()
    offset = db.IntField()
    start = db.IntField()
    end = db.IntField()
    timenode = db.IntField()
    
    def new_event(user,name,frequency,offset,start,end,timenode): # 想写成**kwargs了
        return Event(
            user = user,
            name = name,
            frequency = frequency,
            offset = offset,
            start = start,
            end = end,
            timenode = timenode
        ).save()

    def edit_event(self,name,frequency,offset,start,end,timenode):
        self.name = name
        self.frequency = frequency
        self.offset = offset
        self.start = start
        self.end = end
        self.timenode = timenode
        return self.save()

    def get_by_id(id):
        return Event.objects(id=id).first()

    def get_info(self):
        return {
            "id":str(self.id),
            "frequency":self.frequency,
            "offset":self.offset,
            "start":self.start,
            "end":self.end
        }