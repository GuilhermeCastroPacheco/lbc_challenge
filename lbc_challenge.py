# LEVEL 3
# True se a string estiver balanceada e False se não
# Identifica o erro
# ignora ",", ', " e : 
def isBalanced(str_to_balance):
    special_chars = "()[]{}"
    special_chars_dic = {"(": 1, ")": -1, "[": 2, "]": -2, "{": 3, "}": -3}
    chars = [char for char in str_to_balance if char in special_chars]
    indexes = [i for i in range(len(str_to_balance)) if str_to_balance[i] in special_chars]
    chars_nums = [special_chars_dic[str_to_balance[i]] for i in range(len(str_to_balance)) if str_to_balance[i] in special_chars_dic]

    """print(chars)
    print("".join(chars))
    print(indexes)
    print(chars_nums)"""
    
    if len(indexes) % 2 != 0:
        return (False, 0)
    elif sum(chars_nums) != 0:
        return (False, 1)
    else:
        if chars_nums[0]<0 or chars_nums[0] != -(chars_nums[-1]):
            return (False, 1)
        else:
            aux = 0
            for i in range(1, len(chars_nums)-1):
                if i<aux:
                    continue
                """print(i)
                print(chars_nums[i:].index(-chars_nums[i])+1+i)
                print(sum(chars_nums[i:chars_nums[i:].index(-chars_nums[i])+1+i]))"""
                if chars_nums[i]<0:
                    return (False, 1)
                elif sum(chars_nums[i:chars_nums[i:].index(-chars_nums[i])+1+i]) != 0:
                    return (False, 1)
                elif chars_nums[i+1]<0:
                    aux = i+2
                    if chars_nums[aux] < 0:
                        aux += 1

    return (True, -1)
            
"""def balance(str_to_balance):
    for i in range(len(str_to_balance)):
        if str_to_balance[i] != -(str_to_balance[-i]):
            if str_to_balance[i] != -(str_to_balance[i+1]):
                return True"""
                

if __name__ == "__main__":
    test_strs = ["[{(xxxxxxxx]}", "[{(xxx), (xx)}]", "[{(xxx), (xxx)}, {(xxx), (xxx)}]", "[{(xxx), (xxx)), {(xxx), (xxx)}]", "[{(xxx), (xxx)}, {(xxx), (xxx)]}", "[{(xxx), (xxx)}, {(xxx)}]"]
    # resultado esperado: False (faltam), True, True, False (ordem), False (ordem)
    for test_str in test_strs:
        result = isBalanced(test_str)
        print(result[0])
        if not result[0]:
            if result[1] == 0:
                print("Erro: faltam caracteres especiais")
            else:
                print("Erro: ordem dos caracteres especiais errada")
            #print("Exemplo de string balanceada:\n" + balance(test_str))
            #isBalanced(balance(test_str))