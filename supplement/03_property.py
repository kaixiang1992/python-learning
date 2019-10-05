'''
@description 【Python知识补充】get和set方法 2019/10/05 14:48
'''

class Plane(object):
    def __init__(self):
        # TODO: 存活状态
        self.alive = True
        # TODO: 累计积分
        self.score = 0
    
    # TODO: 更改存活状态
    def set_alive(self, value): 
        self.alive = value
        if value == False:
            self.die_action()
    
    # TODO: 获取存活状态
    def get_alive(self):
        if not self.alive:
            self.cancel_schedule()
        return self.alive

    # TODO: 设置累计积分
    def set_score(self, value):
        self.score = value
        self._update_score_ranking(value)

    # TODO: 更新积分排行榜
    def _update_score_ranking(self, value):
        print('更新积分排行榜：%d'%(value, ))

    # TODO: 执行飞机死亡动画
    def die_action(self):
        print('执行飞机死亡动画!...')
    
    # TODO: 取消事件调度
    def cancel_schedule(self):
        print('取消事件调度!...')

plane = Plane()
# TODO: 击中状态
hit = True 
if hit:
    plane.set_alive(False)
    plane.set_score(150)
    plane.get_alive()