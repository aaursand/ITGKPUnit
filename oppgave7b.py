import unittest

def check_equal(str1, str2):
    if(not len(str1)==len(str2)):
        return False
    for i in range(len(str1)):
        if(str1[i]!=str2[i]):
            return False
    return True

def reversed_word(str1):
    new_word = ""
    for i in range(len(str1)):
        new_word += str1[len(str1)-1-i]
    return new_word


def check_palindrome(str1):
    rword = reversed_word(str1)
    return check_equal(str1,rword)

def contains_string(str1, str2):
    return str1.find(str2)

            



class TestMethods(unittest.TestCase):

	def test_1(self):
            str1 = 'hei'
            str2 = 'hello'
            str3 = 'hello'
            stud_answer = check_equal(str1, str2)
            stud_answer2 = check_equal(str3, str2)
	    self.assertEqual(stud_answer, False)
	    self.assertEqual(stud_answer2, True)

	def test_2(self):
            str8 = 'Morna Jens'
            self.assertEqual(reversed_word(str8), "sneJ anroM")

            str1 = 'agnes i senga'
            str2 = 'hello'
            self.assertEqual(check_palindrome(str1), True)

        def test_4(self):
            str1 = 'pepperkake'
            str2 = 'per'
            str3 = 'ola'
            self.assertEqual(contains_string(str1, str2),3)
            self.assertEqual(contains_string(str1, str3),-1)

            

if __name__ == '__main__':
	unittest.main()
