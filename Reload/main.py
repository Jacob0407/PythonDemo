# -*- coding: utf-8 -*-
import importlib
import Reload.TestModule


print("======== before ========")
print("module's id: ", id(Reload.TestModule))
print(id(Reload.TestModule.var_1))
print(id(Reload.TestModule.var_2))
print(id(Reload.TestModule.var_3))
print(id(Reload.TestModule.var_4))
print(id(Reload.TestModule.var_5))
print(id(Reload.TestModule.var_6))
print(id(Reload.TestModule.var_7))

input_data = input("enter:")

importlib.reload(Reload.TestModule)

print("======== after! ========")
print("module's id: ", id(Reload.TestModule))
print(id(Reload.TestModule.var_1))
print(id(Reload.TestModule.var_2))
print(id(Reload.TestModule.var_3))
print(id(Reload.TestModule.var_4))
print(id(Reload.TestModule.var_5))
print(id(Reload.TestModule.var_6))
print(id(Reload.TestModule.var_7))
print(id(getattr(Reload.TestModule, "var_8")))
