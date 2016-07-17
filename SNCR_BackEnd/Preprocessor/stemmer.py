

class stemm(object):

    def stemminig(doc) :
        doc.sort()
        list = []
        list = doc
        i = 0
        print("list length ==========="+str(len(list)))
        same = []

        while (i < len(list)):
            j = i + 1
            while (j < len(list)):
                u = zip(list[i], list[j])
                d = dict(u)
                x=[]
                for k,m in d.items():
                    if k == m:
                        # same.append(j)
                        # del list[j]
                        # list.sort()
                        x.append(j)
                    # else:
                    #     break
                    # if (doc[i] in doc[j]) :
                    #
                    #     print("okkkkkkkkkkkkkkkk")
                    #     print("first %s and second %s"%(doc[i],doc[j]))
                # p = (len(x)*2) / (len(doc[i]) + len(doc[j]))
                p =len(x)/len(d)
                # print(doc[i]+" and "+doc[j]+" are same in "+str(p))
                if p > 0.5:
                    print(doc[i] +" = "+doc[j])
                    del list[j]
                    j -= 1
                j += 1
            i+=1
        #
        # n=0
        # while (n < len(same)):
        #     # del list[same[n]]
        #     print("###################"+str(same[n]))
        #     n+=1
        #
        n = 0
        while (n < len(list)):
            print('@@@@@@@@@@@@'+list[n])
            n += 1