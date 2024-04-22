# from openpyxl import load_workbook
# wb=load_workbook("C:\\Users\\shashi\\Desktop\\ExcelSheet.xlsx")
# sh=wb['Login']
# print(sh['A1'].value)
# print(wb['Login']['A2'].value)
# print("----------------------------")
# print(sh.cell(1,1).value)
# print(sh.cell(1,2).value)
# print(sh.cell(2,1).value)
# print(sh.cell(2,2).value)
# print("----------------------------")
# print(sh.cell(row=2,column=2).value)
# print(sh.cell(row=3,column=3).value)


# 2)--------------------------------------
# from openpyxl import load_workbook
# wb=load_workbook("C:\\Users\\shashi\\Desktop\\ExcelSheet.xlsx")
# sh=wb['Login']
# rowcount=sh.max_row
# columncount=sh.max_column
# for i in range(1,rowcount+1):
#     for j in range(1,columncount+1):
#         print(sh.cell(i,j).value,end='  ')
#     print()

# # How to remove lines starting with any prefix using Python?
# def meth():
#
#     with open("C:\\Users\\shashi\\Desktop\\abc.txt")as f:
#         content=f.readlines()
#         for lines in content:
#             if lines.startswith("my"):
#                 print(lines)
#             if not (lines.startswith("my")):
#                 print(lines)
# meth()

# # Eliminating repeated lines from a file using Python-------------------------------
# def meth2():
#     inputfile=open("C:\\Users\\shashi\\Desktop\\abc.txt","r")
#     outputfile=open("C:\\Users\\shashi\\Desktop\\xyz22.txt","w")
#     lines_already_visited=set()
#     for line in inputfile:
#         if line not in lines_already_visited:
#             outputfile.write(line)
#             lines_already_visited.add(line)
#
#     print(lines_already_visited)
#     print('\n')
#     inputfile.close()
#     outputfile.close()
#
# meth2()


# Read List of Dictionaries from File in Python---------------------------
import pickle
def meth3():
    try:
        newfile = open('C:/Users/shashi/Desktop/aaa.txt', 'r')
        dictionary_list = pickle.load(newfile)

        for d in dictionary_list:
            print(d)
        newfile.close()

    except:
        print("Something unexpected occurred!")


meth3()








