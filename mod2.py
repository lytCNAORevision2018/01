# Excel中的数据导入本程序。
import pandas as pd
df = pd.read_excel('Python招聘数据（全）.xlsx')
# 学生的参与-专注模型
#模型的第一部分：学生的专注-参与模型。
# sheet_data_1 = work_book["Sheet1"]
t_0 = float(input('请输入每节课的时长。'))
t_n = float(df['学生的专注时间'])
tn_2 = float(df['学生深度参与的时间'])
n_0 = float(df(['课程数']).values)
p = float(df['本专业最高学分'].values)
k2 = float(df['考研相关度'].values)
phi = float(input('请输入本专业本方向历年考研率的算数平均值。'))
lamda = float(df['改正项系数'].values)
miu = float(df['课程类型-内容改正项'].values)
k3 = float(df['考核难度系数'].values)
k4 = float(df['课程与毕业要求关系系数'].values)
m = float(df['课程学分'].values)
p_2 = float(df['本专业最高学分'].values)
k1 = m/p_2
import math
# 注意：以上k1,k2,k3,k4输入0~1之间的小数，lamda、miu、phi三个值可输入超过1的数。
k = k1+phi^(-1)*lamda*k2+miu*k3+k4
def participation_attention():
    math.log(k) * (t_n + tn_2) * n_0 / t_0
  for i in range(int(n_0)):
      i+= 1
      A = math.log(k) * (t_n + tn_2) * n_0 / t_0
      A=A+ 1
      print(A)
else:
    print('A函数的值已经输出。')
#############################
a1 = float(df['考生高考排名'].values)
a2 = float(df['全省高考人数'].values)
b1 = float(df['外语分级测试排名'].values)
b2 = float(df['参加外语测试人数'].values)
c1 = float(df['考核难度系数'].values)
c2 = float(df['考核难度系数'].values)
c3 = float(df['考核难度系数'].values)
alpha = float(df['考核难度系数'].values)
beta = float(df['新生外语成绩权重'].values)
u = input('请输入考生高考的类型')
if u =='文科':
    d1 = float(df['语文难度系数'].values)
    d2 = float(df['考生的语文成绩'].values)
    d3 = float(df['当地语文满分'].values)
    gamma = float(df['高考语文成绩权重'].values)
    B = alpha * (a1 / a2)^(-1) + beta* (b1 / b2)^(-1) + gamma * (c1 * c2 / c3)
elif u== '理科':
    e1 = float(df['数学难度系数'].values)
    e2 = float(df['考生的数学成绩'].values)
    e3 = float(df['当地数学满分'].values)
    delta: float = float(df['高考数学成绩权重'].values)
    B = alpha*(a1/a2)^(-1)+beta*(b1/b2)^(-1)+delta*(e1*e2/e3)
else:
    print('请重新输入！')
############################