import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.length = int(800*K)
        self.width = int(600*K)
        self.canvas = tk.Canvas(width=self.width*1.5, height=self.length, bg=Canvas_C1)
        self.canvas.pack()
        self.set_labels()
        self.title("氢能耦合直流互联系统仿真验证平台")        
        self.minsize(self.length,self.width) # 最小尺寸
        self.maxsize(self.length,self.width) # 最大尺寸
        self.geometry("%sx%s"%(self.length,self.width))
        self.set_buttons()
        
        self.logo1 = tk.PhotoImage(file=r"../logo1_size2.png")
        #self.logo1.config(width=275,height=179)
        self.logo_label1 = tk.Label(self, image = self.logo1,bg=Canvas_C1)
        self.logo_label1.place(x=260,y=160)
        
        self.logo2 = tk.PhotoImage(file=r"../logo2_size2.png")
        #self.logo1.config(width=275,height=179)
        self.logo_label2 = tk.Label(self, image = self.logo2,bg=Canvas_C1)
        self.logo_label2.place(x=260,y=360)
        
    
    def set_labels(self):
        self.title_label = tk.Label(self, text="氢能耦合直流互联系统仿真验证平台",bg=Canvas_C1,fg=Font_C1,font=('宋体','30'))
        self.title_label.place(x=80*K,y=30*K,)
        
        self.acknowledgment = tk.Label(self, text="致谢：感谢国家重点研发项目《可离网型风/光/氢燃料电池直流互联与稳定控制技术》",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15',"bold"))
        self.acknowledgment.place(x=40*K,y=520*K,)
        
    def set_buttons(self):
        X_1 = 80 * K
        X_2 = 550 * K
        Y = 150 * K
        DY = 100 * K
        # 结构配置
        self.ST_button = tk.Button(self, text = '结构配置',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','20'),command=self.showST)
        self.ST_button.place(x=X_1,y=Y)
        # 参数配置
        self.PA_button = tk.Button(self, text = '参数配置',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','20'),command=self.showPA)
        self.PA_button.place(x=X_1,y=Y+1*DY)
        # 环境配置
        self.EV_button = tk.Button(self, text = '环境配置',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','20'),command=self.showEV)
        self.EV_button.place(x=X_1,y=Y+2*DY)
        # 用户配置
        self.US_button = tk.Button(self, text = '用户配置',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','20'),command=self.showUS)
        self.US_button.place(x=X_1,y=Y+3*DY)
        # 暂态仿真
        self.TS_button = tk.Button(self, text = '暂态仿真',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','20'))
        self.TS_button.place(x=X_2,y=Y)
        # 稳态仿真
        self.SS_button = tk.Button(self, text = '稳态计算',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','20'))
        self.SS_button.place(x=X_2,y=Y+1*DY)
        # 优化配置
        self.OP_button = tk.Button(self, text = '优化配置',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','20'),command=self.showOP)
        self.OP_button.place(x=X_2,y=Y+2*DY)
        # 稳定性分析
        self.SA_button = tk.Button(self, text = '稳定性分析',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','20'),command=self.showSA)
        self.SA_button.place(x=X_2,y=Y+3*DY)
    
    def showST(self):
        global ST_win
        ST_win = ST_Win()
        ST_win.mainloop()
    def showPA(self):
        PA_Win().mainloop()
    def showEV(self):
        PV_Win().mainloop()
    def showUS(self):
        US_Win().mainloop()
    def showOP(self):
        OP_Win().mainloop()
    def showSA(self):
        SA_Win().mainloop()

class ST_Win(tk.Tk):
    def __init__(self):
        super().__init__()
        self.bus_num = 0
        self.length = mainwindow.length
        self.width = mainwindow.width
        self.configure(bg=Canvas_C1)
        self.title("结构配置")        
        self.minsize(self.length,self.width) # 最小尺寸
        self.maxsize(self.length,self.width) # 最大尺寸
        self.geometry("%sx%s"%(self.length,self.width))
        self.set_labels()
        self.set_buttons()
        self.set_text()
        self.set_var()
        
    
    def set_labels(self):
        self.title_label = tk.Label(self, text="结构配置",bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','30'),width=10,height=1)
        self.title_label.place(x=260*K,y=30*K,)
        self.text_label = tk.Label(self, text="结构配置状态表",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=30,height=1)
        self.text_label.place(x=50*K,y=220*K,)
        self.text_label = tk.Label(self, text="选择母线类型",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
        self.text_label.place(x=20*K,y=110*K,)

    def set_buttons(self):
        self.OK_button = tk.Button(self, text = '确定',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','20'),command=self.closeWin)
        self.OK_button.place(x=400*K,y=520*K)
        self.Quit_button = tk.Button(self, text = '取消',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','20'),command=self.closeWin)
        self.Quit_button.place(x=600*K,y=520*K)
        self.addbus_button = tk.Button(self, text = '添加母线',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),command=self.addbus)
        self.addbus_button.place(x=150*K,y=160*K)
        self.defconn_button = tk.Button(self, text = '定义连接方式',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','20'),command=self.show_conn_def)
        self.defconn_button.place(x=560*K,y=100*K)
    
    def set_text(self):
        self.text_1 = tk.Text(self, width=int(50/1.2), height=int(20/1.2),font=textfont)
        self.text_1.place(x=40*K,y=250*K,)
        
    def set_var(self):
        self.var = tk.StringVar()     # #创建变量，便于取值 
        self.com = ttk.Combobox(self, textvariable=self.var,)     # #创建下拉菜单
        self.com.place(x=150*K,y=110*K)     # #将下拉菜单绑定到窗体
        self.com["value"] = ("10kV", "375V")
        self.com.current(0)
        
    def closeWin(self):
        self.destroy()
        
    def addbus(self):
        self.bus_num += 1
        self.text_1.insert(tk.INSERT,'母线%s已添加,类型为%s\n'%(self.bus_num,self.com.get()))

    def show_conn_def(self):
        Conn_def().mainloop()
    
    def showtable(self):
        tree=ttk.Treeview(self)
        tree.place(x=420*K,y=250*K,)
        #定义列
        tree["columns"]=("BUS1","BUS2","BUS3")
        #设置列属性，列不显示
        tree.column("BUS1",width=30, anchor = "center")
        tree.column("BUS2",width=30, anchor = "center")
        tree.column("BUS3",width=30, anchor = "center")
        
        
        #设置表头
        tree.heading("BUS1",text="母线1")
        tree.heading("BUS2",text="母线2")
        tree.heading("BUS3",text="母线3")
        
        if conn_type1==0 :
            value_12 = conn_R1
        elif conn_type1 ==-1:
            value_12 = conn_type1
            
        if conn_type2==0 :
            value_13 = conn_R2
        elif conn_type2 ==-1:
            value_13 = conn_type2
            
        if conn_type3==0 :
            value_23 = conn_R3
        elif conn_type3 ==-1:
            value_23 = conn_type3
            
        #print(conn_type1,conn_type2,conn_type3)
        #添加数据
        tree.insert("",0,text="母线1",values=("0",str(value_12),str(value_13),))#  0 为列的下标，第0行
        tree.insert("",1,text="母线2",values=(str(value_12),"0",str(value_23),))
        tree.insert("",2,text="母线3",values=(str(value_13),str(value_23),"0",))
     
        
class Conn_def(tk.Tk):
    def __init__(self):
        super().__init__()
        self.length = int(mainwindow.length/2)
        self.width = int(mainwindow.width/2)
        self.configure(bg=Canvas_C1)
        self.title("连接方式定义")        
        self.minsize(self.length,self.width) # 最小尺寸
        self.maxsize(self.length,self.width) # 最大尺寸
        self.geometry("%sx%s"%(self.length,self.width))
        self.set_labels()
        self.set_var()
        self.set_buttons()        
        #self.set_text()
        self.add_flag = False
        self.showed_flag = False
        
    def set_labels(self):
        self.label1 = tk.Label(self, text="母线一",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
        self.label1.place(x=5*K,y=20*K,)
        self.label2 = tk.Label(self, text="母线二",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
        self.label2.place(x=180*K,y=20*K,)
        self.label3 = tk.Label(self, text="母线一",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
        self.label3.place(x=5*K,y=60*K,)
        self.label4 = tk.Label(self, text="母线三",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
        self.label4.place(x=180*K,y=60*K,)
        self.label5 = tk.Label(self, text="母线二",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
        self.label5.place(x=5*K,y=100*K,)
        self.label6 = tk.Label(self, text="母线三",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
        self.label6.place(x=180*K,y=100*K,)
    
    def set_var(self):
        global conn1_type,conn2_type,conn3_type,conn1_com,conn2_com,conn3_com
        conn1_type = tk.StringVar()     # #创建变量，便于取值 
        conn1_com = ttk.Combobox(self, textvariable=conn1_type,width=10)     # #创建下拉菜单
        conn1_com.place(x=110*K,y=23*K)     # #将下拉菜单绑定到窗体
        conn1_com["value"] = ("母线直连", "互联变流器")
        conn1_com.current(1)
        
        conn2_type = tk.StringVar()     # #创建变量，便于取值 
        conn2_com = ttk.Combobox(self, textvariable=conn2_type,width=10)     # #创建下拉菜单
        conn2_com.place(x=110*K,y=63*K)     # #将下拉菜单绑定到窗体
        conn2_com["value"] = ("母线直连", "互联变流器")
        conn2_com.current(1)
        
        conn3_type = tk.StringVar()     # #创建变量，便于取值 
        conn3_com = ttk.Combobox(self, textvariable=conn3_type,width=10)     # #创建下拉菜单
        conn3_com.place(x=110*K,y=103*K)     # #将下拉菜单绑定到窗体
        conn3_com["value"] = ("母线直连", "互联变流器")
        conn3_com.current(1)
    
    def set_buttons(self):
        self.add_button1 = tk.Button(self, text = '添加',padx=0,pady=0,width=6,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','10'),command=lambda:self.show_subtable1(con_label=1))
        self.add_button1.place(x=300*K,y=20*K)
        self.add_button2 = tk.Button(self, text = '添加',padx=0,pady=0,width=6,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','10'),command=lambda:self.show_subtable1(con_label=2))
        self.add_button2.place(x=300*K,y=60*K)
        self.add_button3 = tk.Button(self, text = '添加',padx=0,pady=0,width=6,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','10'),command=lambda:self.show_subtable1(con_label=3))
        self.add_button3.place(x=300*K,y=100*K)
    
    def show_subtable1(self,con_label):
        self.add_flag = True
        self.show_subcanvas()
        if eval('conn%s_com.get()'%con_label)=="母线直连":
            self.R_label = tk.Label(self, text="线路电阻",bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
            self.R_label.place(x=30,y=190)
            self.R1_text = tk.Text(self, width=20, height=1)
            self.R1_text.place(x=150*K,y=195*K,)
            
            self.sub_ok1 = tk.Button(self, text = '确认',padx=0,pady=0,width=6,height=1,bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','10'),command=lambda: self.destroy_subcanva11(con_label=con_label,des_type=0))
            self.sub_ok1.place(x=240*K,y=240*K)
            self.sub_cancel1 = tk.Button(self, text = '取消',padx=0,pady=0,width=6,height=1,bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','10'),command=lambda: self.destroy_subcanva11(con_label=con_label,des_type=1))
            self.sub_cancel1.place(x=320*K,y=240*K)
        if eval('conn%s_com.get()'%con_label)=="互联变流器":
            self.port_label = tk.Label(self, text="端口容量",bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','12'),width=10,height=1)
            self.port_label.place(x=30,y=150)
            self.control_label1 = tk.Label(self, text="移相控制",bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','12'),width=10,height=1)
            self.control_label1.place(x=30,y=180)
            self.control_label2 = tk.Label(self, text="控制方式",bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','12'),width=10,height=1)
            self.control_label2.place(x=30,y=210)
            self.port_text = tk.Text(self, width=20, height=1)
            self.port_text.place(x=150*K,y=155*K,)
            self.control_text = tk.Text(self, width=20, height=1)
            self.control_text.place(x=150*K,y=185*K,)
            
            global conn1_control_com
            conn1_control_type = tk.StringVar()     # #创建变量，便于取值 
            conn1_control_com = ttk.Combobox(self, textvariable=conn1_control_type,width=15)     # #创建下拉菜单
            conn1_control_com.place(x=150*K,y=210*K)     # #将下拉菜单绑定到窗体
            conn1_control_com["value"] = ("控制方式1", "控制方式2")
            conn1_control_com.current(1)

            self.sub_ok1 = tk.Button(self, text = '确认',padx=0,pady=0,width=6,height=1,bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','10'),command=lambda:self.destroy_subcanva12(con_label=con_label,des_type=1))
            self.sub_ok1.place(x=240*K,y=240*K)
            self.sub_cancel1 = tk.Button(self, text = '取消',padx=0,pady=0,width=6,height=1,bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','10'),command=lambda:self.destroy_subcanva12(con_label=con_label,des_type=0))
            self.sub_cancel1.place(x=320*K,y=240*K)
    

    
    def show_subcanvas(self):
        self.canvas = tk.Canvas(self,width=375*K, height=140*K, bg=Button_BG_C1)
        self.canvas.place(x=10,y=140)        
        
    
    def destroy_subcanva11(self,con_label,des_type):
        if not des_type:
            global conn_R1,conn_R2,conn_R3,conn_type1,conn_type2,conn_type3
            R = self.R1_text.get("0.0", tk.END)
            if con_label==1:
                conn_R1=R
                conn_type1 = 0
            if con_label==2:
                conn_R2=R
                conn_type2 = 0
            if con_label==3:
                conn_R3=R
                conn_type3 = 0
        self.canvas.destroy()
        self.sub_cancel1.destroy()
        self.sub_ok1.destroy()
        self.R_label.destroy()
        self.R1_text.destroy()
        self.sub_ok1.destroy()
        if self.add_flag and (not self.showed_flag):
            self.show_hidebutton()
            self.showed_flag = True
        
    def destroy_subcanva12(self,con_label,des_type):
        if des_type:
            global conn_type2,conn_type3
            if con_label==1:
                conn_type1 = -1
            if con_label==2:
                conn_type2 = -1
            if con_label==3:
                conn_type3 = -1
        self.canvas.destroy()
        self.sub_cancel1.destroy()
        self.sub_ok1.destroy()
        self.port_label.destroy()
        self.control_label1.destroy()
        self.control_label2.destroy()
        self.port_text.destroy()
        self.control_text.destroy()
        conn1_control_com.destroy()
        if self.add_flag and (not self.showed_flag):
            self.show_hidebutton()
            self.showed_flag = True
        
    
    def show_hidebutton(self):
        self.sub_ok2 = tk.Button(self, text = '确认',padx=0,pady=0,width=6,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','10'),command=self.destroy_subwin)
        self.sub_ok2.place(x=240*K,y=240*K)
    
    def destroy_subwin(self):
        self.destroy()
        ST_win.showtable()
    
class PA_Win(tk.Tk):
    def __init__(self):
        super().__init__()
        self.bus_num = 0
        self.length = int(mainwindow.length)
        self.width = int(mainwindow.width)
        self.configure(bg=Canvas_C1)
        self.title("参数配置")        
        self.minsize(self.length,self.width) # 最小尺寸
        self.maxsize(self.length,self.width) # 最大尺寸
        self.geometry("%sx%s"%(self.length,self.width))
        self.set_labels()
        self.set_var()
        self.set_buttons()
        
        self.set_text()
        #
    
    def set_labels(self):
        self.title_label = tk.Label(self, text="参数配置",bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','30'),width=10,height=1)
        self.title_label.place(x=260*K,y=30*K,)
        self.text_label = tk.Label(self, text="参数配置信息表",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=30,height=1)
        self.text_label.place(x=400*K,y=110*K,)
        self.text_label = tk.Label(self, text="选择设备类型",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
        self.text_label.place(x=20*K,y=110*K,)
    
    def set_var(self):
        self.var2 = tk.StringVar()     # #创建变量，便于取值 
        self.com2 = ttk.Combobox(self, textvariable=self.var2,)     # #创建下拉菜单
        self.com2.place(x=150*K,y=110*K)     # #将下拉菜单绑定到窗体
        self.com2["value"] = ("光伏", "风机","电解水制氢","燃料电池","锂电池","储氢罐")
        self.com2.current(1)
    
    def set_buttons(self):
        self.OK_button = tk.Button(self, text = '确定',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','20'),command=self.closeWin)
        self.OK_button.place(x=400*K,y=520*K)
        self.Quit_button = tk.Button(self, text = '取消',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','20'),command=self.closeWin)
        self.Quit_button.place(x=600*K,y=520*K)
        self.addbus_button = tk.Button(self, text = '添加设备',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),command=self.addequ)
        self.addbus_button.place(x=150*K,y=160*K)
    
    def closeWin(self):
        self.destroy()
    
    def addequ(self):
        #print(1)
        #print( self.com2.get())
        if self.com2.get()=="电解水制氢":
            self.show_t1()
            
    def set_text(self):
        self.text_1 = tk.Text(self, width=int(50/1.2), height=int(20/1.2),font=textfont)
        self.text_1.place(x=420*K,y=140*K,)
    
    def show_t1(self):
        self.canvas = tk.Canvas(self,width=400*K, height=200*K, bg=Button_BG_C1)
        self.canvas.place(x=10,y=250)
        self.title_label = tk.Label(self, text="电解水制氢",bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','20'),width=10,height=1)
        self.title_label.place(x=120*K,y=255*K,)
        self.label1 = tk.Label(self, text="对应母线：",bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),)
        self.label1.place(x=40*K,y=300*K,)
        self.label2 = tk.Label(self, text="电解池数：",bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),)
        self.label2.place(x=40*K,y=330*K,)
        self.label3 = tk.Label(self, text="极板面积：",bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),)
        self.label3.place(x=40*K,y=360*K,)
        
        self.label7 = tk.Label(self, text="型号设置：",bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),)
        self.label7.place(x=40*K,y=390*K,)
        
        self.label4 = tk.Label(self, text="极板间距：",bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),)
        self.label4.place(x=220*K,y=300*K,)
        self.label5 = tk.Label(self, text="工作温度：",bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),)
        self.label5.place(x=220*K,y=330*K,)
        self.label6 = tk.Label(self, text="系统压力：",bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),)
        self.label6.place(x=220*K,y=360*K,)
        
        
        self.var1 = tk.StringVar()     # #创建变量，便于取值 
        self.com = ttk.Combobox(self, textvariable=self.var1,width=8)     # #创建下拉菜单
        self.com.place(x=140,y=302)     # #将下拉菜单绑定到窗体
        self.com["value"] = ("母线1", "母线2", "母线3")
        
        self.var3 = tk.StringVar()     # #创建变量，便于取值 
        self.com3 = ttk.Combobox(self, textvariable=self.var3,width=8)     # #创建下拉菜单
        self.com3.place(x=140,y=392)     # #将下拉菜单绑定到窗体
        self.com3["value"] = ("型号1", "型号2", "型号3")
        
        self.text_2 = tk.Text(self, width=10, height=1)
        self.text_2.place(x=140*K,y=335*K,)
        self.text_3 = tk.Text(self, width=10, height=1)
        self.text_3.place(x=140*K,y=365*K,)
        self.text_4 = tk.Text(self, width=10, height=1)
        self.text_4.place(x=320*K,y=305*K,)
        self.text_5= tk.Text(self, width=10, height=1)
        self.text_5.place(x=320*K,y=335*K,)
        self.text_6 = tk.Text(self, width=10, height=1)
        self.text_6.place(x=320*K,y=365*K,)
        
        
        
        self.OK2_button = tk.Button(self, text = '确定',padx=0,pady=0,width=10,height=1,bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','10'),command=self.addequ2)
        self.OK2_button.place(x=200*K,y=420*K)
        self.Quit2_button = tk.Button(self, text = '取消',padx=0,pady=0,width=10,height=1,bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','10'),command=self.closeWin)
        self.Quit2_button.place(x=300*K,y=420*K)
        
    def addequ2(self):
        self.text_1.insert(tk.INSERT,'%s%s已添加至%s\n'%(self.com2.get(),self.com3.get(),self.com.get()))
        
class PV_Win(tk.Tk):
    def __init__(self):
        super().__init__()
        self.bus_num = 0
        self.length = mainwindow.length
        self.width = mainwindow.width
        self.configure(bg=Canvas_C1)
        self.title("环境配置")        
        self.minsize(self.length,self.width) # 最小尺寸
        self.maxsize(self.length,self.width) # 最大尺寸
        self.geometry("%sx%s"%(self.length,self.width))
        self.set_labels()
        self.set_var()
        self.set_buttons()      
        self.set_text()
    
    def set_labels(self):
        self.title_label = tk.Label(self, text="环境配置",bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','30'),width=10,height=1)
        self.title_label.place(x=260*K,y=30*K,)
        self.text_label = tk.Label(self, text="环境配置信息表",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=30,height=1)
        self.text_label.place(x=400*K,y=110*K,)
        self.text_label = tk.Label(self, text="选择导出类型",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
        self.text_label.place(x=20*K,y=320*K,)
        
    def set_buttons(self):
        self.OK_button = tk.Button(self, text = '确定',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','20'),command=self.closeWin)
        self.OK_button.place(x=400*K,y=520*K)
        self.Quit_button = tk.Button(self, text = '取消',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','20'),command=self.closeWin)
        self.Quit_button.place(x=600*K,y=520*K)
        self.EVINPUT_button = tk.Button(self, text = '环境文本输入',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),command=self.add_EV)
        self.EVINPUT_button.place(x=150*K,y=160*K)
        self.LOAD_button = tk.Button(self, text = '负荷数据输入',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),command=self.add_Load)
        self.LOAD_button.place(x=150*K,y=240*K)
        self.Export_button = tk.Button(self, text = '导出',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),command=self.export)
        self.Export_button.place(x=150*K,y=400*K)
    
    def set_var(self):
        
        self.var2 = tk.StringVar()     # #创建变量，便于取值 
        self.com2 = ttk.Combobox(self, textvariable=self.var2,)     # #创建下拉菜单
        self.com2.place(x=150*K,y=330*K)     # #将下拉菜单绑定到窗体
        self.com2["value"] = ("时", "分","秒")
        self.com2.current(0)
        
        
    def closeWin(self):
        self.destroy()
        
    def set_text(self):
        self.text_1 = tk.Text(self, width=int(50/1.2), height=int(20/1.2),font=textfont)
        self.text_1.place(x=420*K,y=160*K,)
        
    def add_EV(self):
        self.text_1.insert(tk.INSERT,'环境文本已添加\n')
    def add_Load(self):
        self.text_1.insert(tk.INSERT,'负载数据已添加\n')
    def export(self):
        self.text_1.insert(tk.INSERT,'已经以 %s 形式导出\n'%self.com2.get())
        
class US_Win(tk.Tk):
    def __init__(self):
        super().__init__()
        self.bus_num = 0
        self.length = mainwindow.length
        self.width = mainwindow.width
        self.configure(bg=Canvas_C1)
        self.title("用户配置")        
        self.minsize(self.length,self.width) # 最小尺寸
        self.maxsize(self.length,self.width) # 最大尺寸
        self.geometry("%sx%s"%(self.length,self.width))
        self.set_labels()
        self.set_text()
        self.set_var()
        self.set_buttons()      
        #
    
    def set_labels(self):
        self.title_label = tk.Label(self, text="用户配置",bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','30'),width=10,height=1)
        self.title_label.place(x=260*K,y=30*K,)
        self.text_label = tk.Label(self, text="用户配置信息表",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=30,height=1)
        self.text_label.place(x=400*K,y=280*K,)
        self.al_label = tk.Label(self, text="选择算法",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
        self.al_label.place(x=400*K,y=100*K,)
        self.kernel_label = tk.Label(self, text="选择并行核",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
        self.kernel_label.place(x=400*K,y=200*K,)
        self.st_label = tk.Label(self, text="仿真开始时间",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
        self.st_label.place(x=50*K,y=100*K,)
        self.et_label = tk.Label(self, text="仿真结束时间",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
        self.et_label.place(x=50*K,y=200*K,)
        self.et_label = tk.Label(self, text="步长",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
        self.et_label.place(x=50*K,y=300*K,)
    
    def closeWin(self):
        self.destroy()
    def set_text(self):   
        self.st = tk.Text(self, width=10, height=2)
        self.st.insert("insert", "0.0s")
        self.st.place(x=200*K,y=100*K,)
        self.et = tk.Text(self, width=10, height=2)
        self.et.place(x=200*K,y=200*K,)
        self.et.insert("insert", "5.0s")
        self.stept = tk.Text(self, width=10, height=2)
        self.stept.place(x=200*K,y=300*K,)
        self.stept.insert("insert", "0.01s")
        self.text = tk.Text(self, width=int(50/1.2), height=int(12/1.2),font=textfont)
        self.text.place(x=400*K,y=320*K,)
        
    def set_var(self):
        
        self.var1 = tk.StringVar()     # #创建变量，便于取值 
        self.com1 = ttk.Combobox(self, textvariable=self.var1,width=10)     # #创建下拉菜单
        self.com1.place(x=520*K,y=110*K)     # #将下拉菜单绑定到窗体
        self.com1["value"] = ("欧拉方法", "龙格-库塔算法")
        self.com1.current(0) 
        self.var2 = tk.StringVar()     # #创建变量，便于取值 
        self.com2 = ttk.Combobox(self, textvariable=self.var2,width=5)     # #创建下拉菜单
        self.com2.place(x=520*K,y=210*K)     # #将下拉菜单绑定到窗体
        self.com2["value"] = ("2", "4","6","8")
        self.com2.current(0) 
    
    def set_buttons(self):
        self.OK_button = tk.Button(self, text = '确定',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','20'),command=self.closeWin)
        self.OK_button.place(x=400*K,y=520*K)
        self.Quit_button = tk.Button(self, text = '取消',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','20'),command=self.closeWin)
        self.Quit_button.place(x=600*K,y=520*K)
        self.EVINPUT_button = tk.Button(self, text = '添加算法',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),command=self.add_al)
        self.EVINPUT_button.place(x=650*K,y=100*K)
        self.LOAD_button = tk.Button(self, text = '添加核数',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),command=self.add_kernel)
        self.LOAD_button.place(x=650*K,y=200*K)
        #self.Export_button = tk.Button(self, text = '导出',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),command=self.export)
        #self.Export_button.place(x=150*K,y=400*K)
    
    def add_al(self):
        self.text.insert(tk.INSERT,'算法已添加\n')
    def add_kernel(self):
        self.text.insert(tk.INSERT,'并行计算已添加\n')
        
class OP_Win(tk.Tk):
    def __init__(self):
        super().__init__()
        self.bus_num = 0
        self.length = mainwindow.length
        self.width = mainwindow.width
        self.configure(bg=Canvas_C1)
        self.title("优化配置")        
        self.minsize(self.length,self.width) # 最小尺寸
        self.maxsize(self.length,self.width) # 最大尺寸
        self.geometry("%sx%s"%(self.length,self.width))
        self.set_labels()
        self.set_text()
        self.set_var()
        self.set_buttons()      
        #
    
    def set_labels(self):
        self.title_label = tk.Label(self, text="优化配置",bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','30'),width=10,height=1)
        self.title_label.place(x=260*K,y=30*K,)
        self.text_label = tk.Label(self, text="优化配置信息表",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=30,height=1)
        self.text_label.place(x=440*K,y=180*K,)
        self.al_label = tk.Label(self, text="优化场景",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
        self.al_label.place(x=430*K,y=100*K,)
        self.st_label = tk.Label(self, text="优化时间长度",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
        self.st_label.place(x=50*K,y=100*K,)
        self.et_label = tk.Label(self, text="时间尺度",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
        self.et_label.place(x=50*K,y=200*K,)
        self.et_label = tk.Label(self, text="优化算法",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
        self.et_label.place(x=50*K,y=300*K,)
        self.oppath = tk.Label(self, text="优化结果路径",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
        self.oppath.place(x=50*K,y=400*K,)
        
    def closeWin(self):
        self.destroy()
    def set_text(self):   
        self.text = tk.Text(self, width=int(50/1.2), height=int(10/1.2),font=textfont)
        self.text.place(x=430*K,y=220*K,)
        self.path = tk.Text(self, width=30, height=2)
        self.path.place(x=200*K,y=400*K,)
        
    def set_var(self):
        self.var1 = tk.StringVar()     # #创建变量，便于取值 
        self.com1 = ttk.Combobox(self, textvariable=self.var1,width=12)     # #创建下拉菜单
        self.com1.place(x=180*K,y=110*K)     # #将下拉菜单绑定到窗体
        self.com1["value"] = ("10年", "20年")
        self.com1.current(0)
        
        
        
        self.var2 = tk.StringVar()     # #创建变量，便于取值 
        self.com2 = ttk.Combobox(self, textvariable=self.var2,width=12)     # #创建下拉菜单
        self.com2.place(x=180*K,y=210*K)     # #将下拉菜单绑定到窗体
        self.com2["value"] = ( "1h", "2h","5h")
        self.com2.current(0)        
        
        self.var3 = tk.StringVar()     # #创建变量，便于取值 
        self.com3 = ttk.Combobox(self, textvariable=self.var3,width=12)     # #创建下拉菜单
        self.com3.place(x=180*K,y=310*K)     # #将下拉菜单绑定到窗体
        self.com3["value"] = (  "Gurobi", "层次聚类","medoid")
        self.com3.current(0)        
        
        self.var4 = tk.StringVar()     # #创建变量，便于取值 
        self.com4 = ttk.Combobox(self, textvariable=self.var4,width=14)     # #创建下拉菜单
        self.com4.place(x=560*K,y=110*K)     # #将下拉菜单绑定到窗体
        self.com4["value"] = (  "典型天气负荷场景", "并离网场景","需求侧激励场景")
        self.com4.current(0) 

    def set_buttons(self):
        self.OK_button = tk.Button(self, text = '开始优化',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','20'),command=self.closeWin)
        self.OK_button.place(x=400*K,y=520*K)
        self.Quit_button = tk.Button(self, text = '取消',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','20'),command=self.closeWin)
        self.Quit_button.place(x=600*K,y=520*K)
        self.INPUT1_button = tk.Button(self, text = '添加',padx=0,pady=0,width=6,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),command=self.add1)
        self.INPUT1_button.place(x=330*K,y=100*K)
        self.INPUT2_button = tk.Button(self, text = '添加',padx=0,pady=0,width=6,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),command=self.add2)
        self.INPUT2_button.place(x=330*K,y=200*K)
        self.INPUT3_button = tk.Button(self, text = '添加',padx=0,pady=0,width=6,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),command=self.add3)
        self.INPUT3_button.place(x=330*K,y=300*K)
        self.INPUT4_button = tk.Button(self, text = '添加',padx=0,pady=0,width=6,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),command=self.add4)
        self.INPUT4_button.place(x=700*K,y=100*K)
        
    
    def add1(self):
        self.text.insert(tk.INSERT,'优化时间长度已添加\n')
    def add2(self):
        self.text.insert(tk.INSERT,'时间尺度已添加\n')
    def add3(self):
        self.text.insert(tk.INSERT,'优化算法已添加\n')
    def add4(self):
        self.text.insert(tk.INSERT,'优化场景已添加\n')
        
class SA_Win(tk.Tk):
    def __init__(self):
        super().__init__()
        self.bus_num = 0
        self.length = mainwindow.length
        self.width = mainwindow.width
        self.configure(bg=Canvas_C1)
        self.title("稳定性分析")        
        self.minsize(self.length,self.width) # 最小尺寸
        self.maxsize(self.length,self.width) # 最大尺寸
        self.geometry("%sx%s"%(self.length,self.width))
        self.set_labels()
        self.set_text()
        self.set_var()
        self.set_buttons()      
        #
    
    def set_labels(self):
        self.title_label = tk.Label(self, text="稳定性分析",bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','30'),width=10,height=1)
        self.title_label.place(x=260*K,y=30*K,)
        self.text_label = tk.Label(self, text="稳定分析状态表",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=30,height=1)
        self.text_label.place(x=430*K,y=180*K,)
        self.al_label = tk.Label(self, text="稳定分析类型",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
        self.al_label.place(x=50*K,y=100*K,)
        self.st_label = tk.Label(self, text="稳定分析方法",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
        self.st_label.place(x=50*K,y=200*K,)
        self.et_label = tk.Label(self, text="稳定分析场景",bg=Canvas_C1,fg=Font_C1,font=('微软雅黑','15'),width=10,height=1)
        self.et_label.place(x=50*K,y=300*K,)
        
        
    def closeWin(self):
        self.destroy()
    def set_text(self):   
        self.text = tk.Text(self, width=int(50/1.2), height=int(10/1.2),font=textfont)
        self.text.place(x=430*K,y=220*K,)
        
        
    def set_var(self):
        self.var1 = tk.StringVar()     # #创建变量，便于取值 
        self.com1 = ttk.Combobox(self, textvariable=self.var1,width=12)     # #创建下拉菜单
        self.com1.place(x=180*K,y=110*K)     # #将下拉菜单绑定到窗体
        self.com1["value"] = ("小干扰稳定", "大干扰稳定")
        self.com1.current(0)
        
        
        
        self.var2 = tk.StringVar()     # #创建变量，便于取值 
        self.com2 = ttk.Combobox(self, textvariable=self.var2,width=12)     # #创建下拉菜单
        self.com2.place(x=180*K,y=210*K)     # #将下拉菜单绑定到窗体
        if self.com1.get()=="小干扰稳定":
            self.com2["value"] = ( "基于广义动态阻抗模型", "基于耦合因子非线性解耦")
            self.com2.current(0)
        elif self.com1.get()=="大干扰稳定":
            self.com2["value"] = ( "基于广义动态阻抗模型", "基于耦合因子非线性解耦")
            self.com2.current(0)            
        
        self.var3 = tk.StringVar()     # #创建变量，便于取值 
        self.com3 = ttk.Combobox(self, textvariable=self.var3,width=12)     # #创建下拉菜单
        self.com3.place(x=180*K,y=310*K)     # #将下拉菜单绑定到窗体
        if self.com1.get()=="小干扰稳定":
            self.com3["value"] = (  "负荷增减", "运行/线路参数微变")
            self.com1.current(0)
        elif self.com1.get()=="大干扰稳定":
            self.com3["value"] = (  "大负荷投切","分布式电源出力突变")
            self.com1.current(0)            
        

    
    def set_buttons(self):
        self.OK_button = tk.Button(self, text = '确定',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','20'),command=self.closeWin)
        self.OK_button.place(x=400*K,y=520*K)
        self.Quit_button = tk.Button(self, text = '取消',padx=0,pady=0,width=10,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','20'),command=self.closeWin)
        self.Quit_button.place(x=600*K,y=520*K)
        self.INPUT1_button = tk.Button(self, text = '添加',padx=0,pady=0,width=6,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),command=self.add1)
        self.INPUT1_button.place(x=330*K,y=100*K)
        self.INPUT2_button = tk.Button(self, text = '添加',padx=0,pady=0,width=6,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),command=self.add2)
        self.INPUT2_button.place(x=330*K,y=200*K)
        self.INPUT3_button = tk.Button(self, text = '添加',padx=0,pady=0,width=6,height=1,bg=Button_BG_C1,fg=Font_C1,font=('微软雅黑','15'),command=self.add3)
        self.INPUT3_button.place(x=330*K,y=300*K)
        
        
    
    def add1(self):
        self.text.insert(tk.INSERT,'稳定分析类型已添加\n')
    def add2(self):
        self.text.insert(tk.INSERT,'稳定分析方法已添加\n')
    def add3(self):
        self.text.insert(tk.INSERT,'稳定分析场景已添加\n')
            
        
K = 1.0 # Global Scale Factor
Font_C1 = 'black'
Button_BG_C1 = 'DarkSeaGreen'
Canvas_C1 = 'Beige'
textfont=('宋体','12')
conn_type1,conn_type2,conn_type3 = -1,-1,-1




mainwindow = MainWindow()
mainwindow.mainloop()

