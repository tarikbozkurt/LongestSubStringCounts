'''
Problem:
t and z are strings consist of lowercase English letters.

Find all substrings for t, and return the maximum value of [ len(substring) x [how many times the substring occurs in z] ]

Example:
t = acldm1labcdhsnd
z = shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa

Solution:
abcd is a substring of t, and it occurs 5 times in Z, len(abcd) x 5 = 20 is the solution

'''


#değerlerimizi aldık
def find_max(string1,string2):
    #tutucu bir string oluşturduk.
    sonuc = ""
    #gelen her bir değer için uzunluklar aldık.
    len1, len2 = len(string1), len(string2)
    
    #başlangıç olarak birinci yani substring uzunluğunca for döngüsü oluşturduk.
    for i in range(len1):
        #eşleşme için kontrol sağlayacağımız str tanımladık
        esitmi = ""
        #string2 için (içerisinde gezeceğimiz string) 
        for j in range(len2):
            """
                    i : 0 
                    j: 0 
                    
                    iteration-1 : 
                                0 < len1(15) 
                                
                                string[i+j] : string[0] :'a' == string2[s]
                                
                                ---> eşitse esitmi +  = string2[0]:s ekle
                                
                                değilse
                                    esitmi ile sonucun uzunlukları aynıysa birbirine eşitle..
                                
                    i : 0 
                    j : 1
                    
                    iteration-2:
                            1 < len1(15) and string1[1] == string2[1]
                                
                                ---> eşitse esitmi +  = string2[1]:h ekle
                                
                                .
                                .
                                .
                                
                     i : 0 
                     j : 2
                    
                    iteration-3:  
                        2 < len1(15) and string1[2] == string2[2]
                        
                        Burada birinci for iterasyon atlayana kadar kontrol yapılır..
                        Gezerken eşit değerler alınır ve eklenir.
                        Substring olan string1 uzunluğuna erişilirse 
                      
                
                
                
                birinci for iterasyon kontrolü
                ------------------------------
                
                i : 1
                
                j : 0 
                
                .
                .
                .
                .
                
            """
            if (i + j < len1 and string1[i + j] == string2[j]):
                esitmi += string2[j]
            else:
                
                if (len(esitmi) > len(sonuc)):
                    sonuc = esitmi
                esitmi = ""
    
  

    return string2.count(sonuc)


if __name__ == '__main__':
    print(find_max("acldm1labcdhsnd","shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa"))
    
    print(len('acldm1labcdhsnd'))
    
