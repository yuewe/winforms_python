#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# 正式环境
BASE_PATH = os.path.split(os.path.realpath(__file__))[0]
if getattr(sys, 'frozen', False):
    BASE_PATH = os.path.dirname(sys.executable)
elif __file__:
    BASE_PATH = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(BASE_PATH, 'libs'))
DOTNET_ROOT = os.path.join(BASE_PATH, 'winforms','dotnet-sdk-6.0.425-win-x64')
WINFORM_DLL_DIR = os.path.join(DOTNET_ROOT,"shared","Microsoft.WindowsDesktop.App","6.0.33")
import platform
release = platform.release().lower()
print(release)

from clr_loader import get_coreclr,get_netfx
from pythonnet import set_runtime
os.environ['DOTNET_ROOT']=DOTNET_ROOT
rt = get_coreclr(runtime_config=os.path.join(WINFORM_DLL_DIR,"Microsoft.WindowsDesktop.App.runtimeconfig.json"))
set_runtime(rt)

sys.path.append(WINFORM_DLL_DIR)

import clr

result = clr.FindAssembly("System.Windows.Forms")
print('FindAssembly returned:', result)
clr.AddReference("System.Windows.Forms")
import System.Windows.Forms as WinForms
from System.Drawing import Size, Point,SizeF,Color,SystemColors,FontStyle,GraphicsUnit,Font
from System import Action,Environment

from Form import Form1
import threading

class WinApp(WinForms.Form):



    def __init__(self):
        super().__init__()

        self.form1 = Form1()
        self.form2 = Form1()

        self.splitContainer1 = WinForms.SplitContainer();
        self.button2 = WinForms.Button();
        self.button1 = WinForms.Button();
        self.button1.Click += lambda sender, args: self.switch_page(sender, args, 'page1')
        self.button2.Click += lambda sender, args: self.switch_page(sender, args, 'page2')
        self.splitContainer1.BeginInit();
        self.splitContainer1.Panel1.SuspendLayout();
        self.splitContainer1.SuspendLayout();
        self.SuspendLayout();
        # //
        # // splitContainer1
        # //
        self.splitContainer1.Anchor = WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Bottom | WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right;
        self.splitContainer1.BorderStyle = WinForms.BorderStyle.FixedSingle;
        self.splitContainer1.Location = Point(5, 3);
        self.splitContainer1.Margin = WinForms.Padding(10);
        self.splitContainer1.Name = "splitContainer1";
        # //
        # // splitContainer1.Panel1
        # //
        self.splitContainer1.Panel1.Controls.Add(self.button2);
        self.splitContainer1.Panel1.Controls.Add(self.button1);
        self.splitContainer1.Size = Size(1186, 553);
        self.splitContainer1.SplitterDistance = 178;
        self.splitContainer1.TabIndex = 0;

        # self.form1.SuspendLayout();
        # self.form1.Anchor = WinForms.AnchorStyles.Top | WinForms.AnchorStyles.Bottom | WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right;

        self.form1.Visible = True;
        self.form2.Visible = False;
        self.form_list = [];
        self.form_list.append(self.form1)
        self.splitContainer1.Panel2.Controls.Add(self.form1);
        self.splitContainer1.Panel2.Controls.Add(self.form2);

        # self.form2.button1.Click += lambda sender, args: self.button_Click(sender, args, 'page2')
        # //
        # // button2
        # //
        self.button2.Anchor = WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right| WinForms.AnchorStyles.Top;
        self.button2.Font = Font("Microsoft YaHei UI", float(12), FontStyle.Regular, GraphicsUnit.Point);
        self.button2.Location = Point(22, 111);
        self.button2.Name = "button2";
        self.button2.Size = Size(136, 47);
        self.button2.TabIndex = 1;
        self.button2.Text = "虎扑";
        self.button2.UseVisualStyleBackColor = True;
        # //
        # // button1
        # //
        self.button1.Anchor = WinForms.AnchorStyles.Left | WinForms.AnchorStyles.Right| WinForms.AnchorStyles.Top;
        self.button1.Font = Font("Microsoft YaHei UI", float(12), FontStyle.Regular, GraphicsUnit.Point);
        self.button1.Location = Point(22, 21);
        self.button1.Name = "button1";
        self.button1.Size = Size(136, 44);
        self.button1.TabIndex = 0;
        self.button1.Text = "豆瓣";
        self.button1.UseVisualStyleBackColor = True;
        # //
        # // Form1
        # //
        self.AutoScaleDimensions = SizeF(float(9), float(20));
        self.AutoScaleMode = WinForms.AutoScaleMode.Font;
        self.ClientSize = Size(1195, 559);
        self.Controls.Add(self.splitContainer1);
        self.Name = "Form1";
        self.Text = "Form1";
        self.splitContainer1.Panel1.ResumeLayout(False);
        self.splitContainer1.EndInit();
        self.splitContainer1.ResumeLayout(False);
        self.ResumeLayout(False);


    def switch_page(self, sender, args,page_type):
        print(f"{sender.Name}:{self.form_list[0].Name}")
        if sender.Name == self.form_list[0].Name:
            return

        if page_type == "page1":

            self.form_list[0].Visible = False;
            self.form1.Visible = True;
            self.form_list.clear()
            self.form_list.append(self.form1)
        if  page_type == "page2":

            self.form_list[0].Visible = False;
            self.form2.Visible = True;
            self.form_list.clear()
            self.form_list.append(self.form2)



    def button_Click(self, sender, args,page_type):

        def update_textbox(text):
            if self.form1.textBox1.InvokeRequired:
                # 如果需要跨线程调用，则使用 Invoke
                self.form1.textBox1.Invoke(Action(lambda: update_textbox(text)))
            else:
                self.form1.textBox1.AppendText(text + Environment.NewLine)
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
    form = WinApp()
    print("form created")
    app = WinForms.Application
    app.SetHighDpiMode(WinForms.HighDpiMode.SystemAware)
    print("app referenced")
    app.Run(form)


if __name__ == '__main__':
    main()