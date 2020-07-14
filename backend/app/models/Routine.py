from app import db
from app.models.User import User
from app.models.Event import Event
import datetime

class Routine(db.Document):
    """
    考虑将每天拆为5块，分别对应课表早上两节课，下午两节课和晚上一节课，
        那么一周的事件可以用长度为固定35的表来表示,
        所以signtime设计为0~34\n
    signtime：\n
        为0~34的整数，表示值班时间段，只在时间段内允许签到\n
    shift：\n
        自主换班时间段，默认和signtime相同，也允许在这个段签到，签完重置为signtime\n
    """
    user = db.ReferenceField(User,reverse_delete_rule=2)
    signtime = db.IntField()
    shift = db.IntField()
    shift_week = db.IntField()

    def init_routine(user:User,signtime:int): # 只在初次用户创建时允许设置signtime
        if Routine.objects(user=user):
            return None
        r = Routine(
            user = user,
            signtime = int(signtime),
            shift = int(signtime)
        )
        return r.save()

    def change_signtime(self,signtime:int): # 不允许低权限用户自主设置
        self.signtime = int(signtime)
        self.shift = self.signtime
        return self.save()

    def recover_shift(self): # 每次换班签到执行后调用，当shift与signtime相等时视为没换班
        self.shift = self.signtime
        return self.save()

    def change_shift(self,shift:int,shift_week:int): # 允许用户自主设置
        self.shift = int(shift)
        self.shift_week = int(shift_week)
        return self.save()

    def get_base_info(self):
        return {
            "user":self.user,
            "signtime":self.signtime,
            "shift":self.shift,
            "shift_week":self.shift_week
        }