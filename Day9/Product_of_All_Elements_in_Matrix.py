def Final_Product(Check_list):
    Prod = 1
    for ele in Check_list:
        Prod *= ele
    return Prod


def Product_Matrix(Test_list):
    Semi_Result = Final_Product(
        [element for ele in Test_list for element in ele])
    return Semi_Result


Test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
print(Product_Matrix(Test_list))
