#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
# import ctypes
# ctypes.windll.shcore.SetProcessDpiAwareness(1)

# 正式环境
BASE_PATH = os.path.split(os.path.realpath(__file__))[0]
if getattr(sys, 'frozen', False):
    BASE_PATH = os.path.dirname(sys.executable)
elif __file__:
    BASE_PATH = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(BASE_PATH, 'libs'))

import threading

# from clr_loader import get_coreclr,get_netfx
# from pythonnet import set_runtime
#
# rt = get_coreclr(runtime_config=r"D:\dotnet\my-dotnet6-win-x64\Microsoft.WindowsDesktop.App.runtimeconfig.json")
# set_runtime(rt)

sys.path.append(r"D:\dotnet\my-dotnet6-win-x64")

import clr

result = clr.FindAssembly("System.Windows.Forms")
print('FindAssembly returned:', result)
clr.AddReference("System.Windows.Forms")
import System.Windows.Forms as WinForms
from System.Drawing import Size, Point,SizeF,Color,SystemColors,FontStyle,GraphicsUnit,Font
from System import Action,Environment


class Form1(WinForms.Form):



    def __init__(self):
        super().__init__()
        self.TopLevel = False; # 设置为非顶级窗口
        self.FormBorderStyle = WinForms.FormBorderStyle(0); #// 移除边框
        self.Dock = WinForms.DockStyle.Fill  # 设置Dock属性为Fill

        self.groupBox1 = WinForms.GroupBox();
        self.button1 = WinForms.Button();
        self.dateTimePicker2 = WinForms.DateTimePicker();
        self.label3 = WinForms.Label();
        self.dateTimePicker1 = WinForms.DateTimePicker();
        self.label2 = WinForms.Label();
        self.comboBox1 = WinForms.ComboBox();
        self.label1 = WinForms.Label();
        self.groupBox2 = WinForms.GroupBox();
        self.textBox1 = WinForms.TextBox();
        self.textBox1.AcceptsReturn = True;
        self.groupBox1.SuspendLayout();
        self.groupBox1.BorderStyle = WinForms.BorderStyle.FixedSingle;


        self.groupBox2.SuspendLayout();
        self.SuspendLayout();
        # //
        # // groupBox1
        # //
        self.groupBox1.Anchor = WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right;
        self.groupBox1.Controls.Add(self.button1);
        self.groupBox1.Controls.Add(self.dateTimePicker2);
        self.groupBox1.Controls.Add(self.label3);
        self.groupBox1.Controls.Add(self.dateTimePicker1);
        self.groupBox1.Controls.Add(self.label2);
        self.groupBox1.Controls.Add(self.comboBox1);
        self.groupBox1.Controls.Add(self.label1);
        self.groupBox1.Font = Font("Microsoft YaHei UI", float(12), FontStyle.Regular, GraphicsUnit.Point);
        self.groupBox1.Location = Point(3, 2);
        self.groupBox1.Name = "groupBox1";
        self.groupBox1.Size = Size(995, 139);
        self.groupBox1.TabIndex = 0;
        self.groupBox1.TabStop = False;
        self.groupBox1.Text = "查询条件";
        # //
        # // button1
        # //
        self.button1.Anchor = WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Bottom;
        self.button1.Location = Point(879, 52);
        self.button1.Name = "button1";
        self.button1.Size = Size(105, 40);
        self.button1.TabIndex = 6;
        self.button1.Text = "开始";
        self.button1.UseVisualStyleBackColor = True;
        self.button1.Click += lambda sender, args: self.button_Click(sender, args, 'page1')
        # //
        # // dateTimePicker2
        # //
        self.dateTimePicker2.Anchor = WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Bottom;
        self.dateTimePicker2.Location = Point(664, 53);
        self.dateTimePicker2.Name = "dateTimePicker2";
        self.dateTimePicker2.Size = Size(182, 33);
        self.dateTimePicker2.TabIndex = 5;
        # //
        # // label3
        # //
        self.label3.Anchor = WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Bottom;
        self.label3.AutoSize = True;
        self.label3.Location = Point(626, 59);
        self.label3.Name = "label3";
        self.label3.Size = Size(32, 27);
        self.label3.TabIndex = 4;
        self.label3.Text = "至";
        # //
        # // dateTimePicker1
        # //
        self.dateTimePicker1.Anchor = WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Bottom;
        self.dateTimePicker1.Location = Point(428, 54);
        self.dateTimePicker1.Name = "dateTimePicker1";
        self.dateTimePicker1.Size = Size(183, 33);
        self.dateTimePicker1.TabIndex = 3;
        # //
        # // label2
        # //
        self.label2.Anchor = WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Bottom;
        self.label2.AutoSize = True;
        self.label2.Location = Point(310, 55);
        self.label2.Name = "label2";
        self.label2.Size = Size(112, 27);
        self.label2.TabIndex = 2;
        self.label2.Text = "督察日期：";
        # //
        # // comboBox1
        # //
        self.comboBox1.Anchor = WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Bottom;
        self.comboBox1.FormattingEnabled = True;
        self.comboBox1.Location = Point(144, 52);
        self.comboBox1.Name = "comboBox1";
        self.comboBox1.Size = Size(151, 35);
        self.comboBox1.TabIndex = 1;
        # //
        # // label1
        # //
        self.label1.Anchor = WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Bottom;
        self.label1.AutoSize = True;
        self.label1.Location = Point(26, 55);
        self.label1.Name = "label1";
        self.label1.Size = Size(112, 27);
        self.label1.TabIndex = 0;
        self.label1.Text = "统计维度：";
        # label1.Click += label1_Click;
        # //
        # // groupBox2
        # //
        self.groupBox2.Anchor = WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Bottom | WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right;
        self.groupBox2.Controls.Add(self.textBox1);
        self.groupBox2.Font = Font("Microsoft YaHei UI", float(12), FontStyle.Regular, GraphicsUnit.Point);
        self.groupBox2.Location = Point(3, 147);
        self.groupBox2.Name = "groupBox2";
        self.groupBox2.Size = Size(995, 359);
        self.groupBox2.TabIndex = 1;
        self.groupBox2.TabStop = False;
        self.groupBox2.Text = "日志";
        # //
        # // textBox1
        # //
        self.textBox1.Anchor = WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Bottom | WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right;
        self.textBox1.BorderStyle = WinForms.BorderStyle.FixedSingle;
        self.textBox1.Location = Point(6, 32);
        self.textBox1.Multiline = True;
        self.textBox1.Name = "textBox1";
        self.textBox1.ScrollBars = WinForms.ScrollBars.Vertical;
        self.textBox1.Size = Size(978, 321);
        self.textBox1.TabIndex = 0;
        # //
        # // Form1
        # //
        self.AutoScaleDimensions = SizeF(float(9), float(20));
        self.AutoScaleMode = WinForms.AutoScaleMode.Font;
        self.ClientSize = Size(999, 506);
        self.Controls.Add(self.groupBox2);
        self.Controls.Add(self.groupBox1);
        self.Name = "Form1";
        self.Text = "Form1";
        self.groupBox1.ResumeLayout(False);
        self.groupBox1.PerformLayout();
        self.groupBox2.ResumeLayout(False);
        self.groupBox2.PerformLayout();
        self.ResumeLayout(False);

    def button_Click(self, sender, args,page_type):

        def update_textbox(text):
            if self.textBox1.InvokeRequired:
                # 如果需要跨线程调用，则使用 Invoke
                self.textBox1.Invoke(Action(lambda: update_textbox(text)))
            else:
                self.textBox1.AppendText(text + Environment.NewLine)
                # self.form1.textBox1.Text = text

        # 定义后台线程要执行的任务
        def background_task():
            result = "更新后的文本"
            # 调用 update_textbox 来更新 UI
            update_textbox(result)

        print(sender)
        """Button click event handler"""
        print ("Click")
        t = threading.Thread(target=background_task, daemon=True)
        t.start()
        # WinForms.MessageBox.Show("Please do not press this button again.")
        # self.Panel5.Visible = False;
        # self.Panel8.Visible = False;
        # self.Panel10.Visible = True;



def main():
    form = Form1()
    print("form created")
    app = WinForms.Application
    # app.set
    print("app referenced")
    app.Run(form)


if __name__ == '__main__':
    main()