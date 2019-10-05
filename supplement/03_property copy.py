'''
@description 【Python知识补充】property装饰器 2019/10/05 15:43
'''

class Plane(object):
    def __init__(self):
        # TODO: 存活状态
        self.__alive = True
        # TODO: 累计积分
        self.__score = 0
    
    # TODO: 获取存活状态
    # 将alive方法设置为属性，然后以后调用temp = p.alive，就会执行这个方法
    @property
    def alive(self):
        if not self.__alive:
            self.cancel_schedule()
        return self.__alive

    # TODO: 更改存活状态
    @alive.setter
    def alive(self, value): 
        self.__alive = value
        if value == False:
            self.die_action()

    @property
    def score(self):
        return self.__score

    # TODO: 设置累计积分
    @score.setter
    def score(self, value):
        self.__score = value
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
    plane.alive = False
    temp = plane.alive
    print(temp)
    plane.score = 100
    plane.score = 200
    plane.score = 300
    score = plane.score
    print(score)