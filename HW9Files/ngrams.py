# -*- coding: utf-8 -*-
"""
Intro to AI -- Analyzing and Generating Text
Nils Napp
University at Buffalo 
"""

from collections import defaultdict,deque,Counter
import numpy as np
import random
import pickle

class Ngrams:
    
    def __init__(self,size=9):
        '''
        N-Gram class to generate n-grams from text files and use them 
        to analyze and generate text. 
        The size argument is the length of the n-grams that are computed 
        from text files. The default (9), means that the n-grams can be used 
        to compute the next character probability given the previous 8
        '''       
  
        assert size>0
        self.maxGram=size-1

        #make training counters
        #could use defaultdict, but then lookups create 0 during testing
        self.ngrams=[]
        for i in range(size):
            self.ngrams.append(Counter())
    
        #call function to set up the character maps
        self._setup() 
        
        #store list of files used during training
        self.fnames=[]
        
        self.scrambledText  =  " xvkndui?d).xc,) nwwnxqv)x ?c,)wxvi" \
                 + ")xfjnw)nd)xd)?jwxdt?m)lwxbm)k?i,w) k,j" \
                 + ",)k,) xv)w,xtndu)x)ijxndndu)v,vvn?db)s" \
                 + "k,scndu)i nii,jm)qjb) nwwnxqvm)x)sy!,j" \
                 + "v,sojniy),hf,jim) xv)tnvqxy,t)i?)tnvs?" \
                 + "a,j)ikxi)k,)kxt)!,,d)ikjovi)ndi?)ik,)q" \
                 + "nttw,)?l)?d,)?l)ik,) ?jvi)v,sojniy)t,!" \
                 + "xsw,v),a,j)i?)!,lxww)xq,jnsxd)ndi,wwnu" \
                 + ",ds,b)qjb) nwwnxqv)kxt) jnii,d)?d)knv)" \
                 + "s?qfxdy)!w?u)x!?oi)ik,)vkxt? )!j?c,jvm" \
                 + ")x)qyvi,jn?ov)uj?of)ikxi)kxt)v?q,k? )?" \
                 + "!ixnd,t)qxdy)?l)ik,)kxscndu)i??wv)ik,)" \
                 + "odni,t)vixi,v)ov,t)i?)vfy)?d)?ik,j)s?o" \
                 + "dijn,vb)d? )ik,)uj?of)kxt)j,fwn,t)nd)x" \
                 + "d)xdujy)vsj,,t)?d)i nii,jb)ni)nt,dinln" \
                 + ",t)knq)s?jj,siwy)xv)x)l?jq,j)q,q!,j)?l" \
                 + ")ik,)dxin?dxw)v,sojniy)xu,dsyv)kxscndu" \
                 + ")uj?ofm)ixnw?j,t)xss,vv)?f,jxin?dvm)?j" \
                 + ")ibxb?bm)x).?!)k,)kxt)d?i)fo!wnswy)tnv" \
                 + "sw?v,tb)ik,d)ik,)vkxt? )!j?c,jv)xvi?dn" \
                 + "vk,t)knq)!y)tj?ffndu)i,skdnsxw)t,ixnwv" \
                 + ")ikxi)qxt,)sw,xj)ik,y)cd, )x!?oi)knukw" \
                 + "y)swxvvnln,t)kxscndu)?f,jxin?dv)ikxi)k" \
                 + ",)kxt)s?dtosi,tb)gik,y)kxt)?f,jxin?dxw" \
                 + ")ndvnuki)ikxi),a,d)q?vi)?l)qy)l,ww? )?" \
                 + "f,jxi?jv)xi)ibxb?b)tnt)d?i)kxa,mg)vxnt" \
                 + ")qjb) nwwnxqvm)d? ) nik)j,dtnin?d)ndl?" \
                 + "v,sm)x)sy!,jv,sojniy)lnjq)k,)l?odt,tb)" \
                 + "gn)l,wi)wnc,)nt)!,,d)cnsc,t)nd)ik,)uoi" \
                 + "b) k?,a,j) j?i,)iknv),nik,j) xv)x) ,ww" \
                 + "fwxs,t)ndvnt,j)?j)kxt)vi?w,d)x)w?i)?l)" \
                 + "?f,jxin?dxw)txixbg)ik,).?wi)i?)qjb) nw" \
                 + "wnxqv)lj?q)ik,)vkxt? )!j?c,jv)jnf?vi,)" \
                 + "xv)fxji)?l)x)qosk)!j?xt,j),xjik'oxc,)i" \
                 + "kxi)kxv)vkxc,d)ik,)dbvbxb)i?)niv)s?j,b" \
                 + ")sojj,di)xdt)l?jq,j)xu,dsy)?llnsnxwv)v" \
                 + "xy)ik,)vkxt? )!j?c,jv)tnvsw?voj,vm) kn" \
                 + "sk)!,uxd)nd)xouovi)m)kxa,)!,,d)sxixvij" \
                 + "?fkns)l?j)ik,)dbvbxbm)sxwwndu)ndi?)'o," \
                 + "vin?d)niv)x!nwniy)i?)fj?i,si)f?i,di)sy" \
                 + "!,j ,xf?dv)xdt)niv)a,jy)axwo,)i?)dxin?" \
                 + "dxw)v,sojniyb)ik,)xu,dsy)j,uxjt,t)xv)i" \
                 + "k,) ?jwtv)w,xt,j)nd)!j,xcndu)ndi?)xta," \
                 + "jvxjn,v)s?qfoi,j)d,i ?jcv)lxnw,t)i?)fj" \
                 + "?i,si)niv)? d"
 
        
        
    '''
    Read a file and add it to the ngrams 
    '''
    def slurpFile(self, fname : str):
        #Go over file a number o times
        
        if not fname in self.fnames:
        
            self.fnames.append(fname)
            
            for gramSize in range(self.maxGram+1):
                
                '''
                dirty char iter ---> Filter (map to charset) ---> ngram iter
                '''
                print(str(gramSize-1) + '-grams: ', end='')
                
                dirtyCharacterIter=self.charIter(fname)
                cleanCharacterIter=self.cleanIter(dirtyCharacterIter)
                
                giter=self.gramIter(cleanCharacterIter, n=gramSize+1)
                
                self.ngrams[gramSize].update(giter)
                
                print(str(sum(self.ngrams[gramSize].values())))

        else:
            print("File already contained in ngram data: " + fname)
                
    def _setup(self):
		     
        #These strings are used to construct a character dict
        #that makes the clean character iterator, this is
        
        abc='abcdefghijklmnopqrstuvwxyz'
        ABC=abc.upper()
        white=' \n\t\r\f\v_'
        punct=".,!?'()"
        quotes='"`“”'  # all the other things that should show up as '
        
        keys=abc+ABC+white+punct+quotes
        vals=abc+abc+'       '+punct+"''''"

        self.charDict=defaultdict(lambda: '',list(zip(iter(keys),iter(vals)))) 

        #remove duplicates
        #these are the characters that can 
        #show up in the clean char iterator
        self.chars=tuple(set(vals))


    def saveGrams(self,fname):
        '''
        grams    : NGRAMS
        chars    : CHARS
        charDict : CHAR_DICT
        maxGram  : MAX_GRAMS
        fileNames: FILE_NAMES
        '''
        
        saveDict=dict([  ['NGRAMS',self.ngrams]
                        ,['CHARS',self.chars]
                        ,['CHAR_DICT',dict(self.charDict)]
                        ,['MAX_GRAMS',self.maxGram]
                        ,['FILE_NAMES',self.fnames]])
        
        with open(fname,'wb') as fh:
            pickle.dump(saveDict,fh)
        

    def loadGrams(self,fname):

        with open(fname,'rb') as fh:
            loadDict=pickle.load(fh,encoding='bytes')            
        
        self.ngrams=loadDict['NGRAMS']
        self.chars=loadDict['CHARS']
        self.charDict=defaultdict(lambda: '', loadDict['CHAR_DICT'])
        self.maxGram=loadDict['MAX_GRAMS']
        self.fnames=['FILE_NAMES']

            
    '''
    return a n iterator that returns single charactres from a file
    '''
    def charIter(self, fname : str):
        
        with open(fname,'r',encoding='UTF8') as fh:
        
            c=fh.read(1)
            
            while not c == '':
                yield c
                c=fh.read(1)                

    '''
    Iterator that returns a cleaned single character
    from an interator that returns non-cleand characters 
    '''
    def cleanIter(self, singleCharIter : iter):

        #if you pass in an empty iterator
        try:
            cnext=next(singleCharIter)
        except StopIteration:
            cnext=''
        
            
        skipWhite=False
        
        while not cnext == '':
            
            if skipWhite:
                if self.charDict[cnext]=='' or self.charDict[cnext]==' ':
                    #print('.')
                    pass
                else:
                    skipWhite=False
                    yield self.charDict[cnext]
            else:
                if self.charDict[cnext]==' ':
                    skipWhite=True
                    #print('Start Skipping')
                    yield ' '
                elif self.charDict[cnext]=='':
                    pass
                else:
                    yield self.charDict[cnext]

            try:
                cnext=next(singleCharIter)
            except StopIteration:
                cnext=''
                       
    '''
    iterator that returns cleaned n-grams
    '''
    def gramIter(self, charIter, n : int = 1):
        
        '''
        Single character iterator that cleans inputs:
            * Only lower case cahracters
            * All white spaces mapped to single ' ' 
            * Limited set of punctuation marks, either ignored or mapped to subset
        '''
        
        #two sided que to shift in and out characters to make n-grams 
        ngramQue=deque()
        
        
        for i in range(n-1):
            try:
                c=next(charIter)
            except StopIteration:
                raise StopIteration
            ngramQue.append(c)                                    
    
        for c in charIter:
            ngramQue.append(c)
            ngram=''.join(e for e in ngramQue)
            yield ngram
            ngramQue.popleft()


    '''
    Return a random character 
    following the given gram according to the n-grams statistics
    
    If the gram + c was never observed for any c then try return 
    a random sample from the last n-1 characters of the n-gram  
    '''
    def nextChar(self, gram : str):
        probs=[]    
        
        randVal=random.random()
        cumulative=0
        
        n=len(gram)
    
        total=0
    
        #build up the list of next options
        for c in self.chars:
            total = total + self.ngrams[n][gram+c]
            probs.append(self.ngrams[n][gram+c])
    
        #if there are not occurances of the gram+c, try the next shorter one
        if total==0:
            return self.nextChar(gram[1:])
    
        else:
            for i in range(len(self.chars)):
                cumulative = cumulative + 1.0*probs[i]/total
                if randVal <= cumulative:
                    return self.chars[i]
        
        #should never get here!!
        #the only way to get here is when all counts of all ngrams are 0
        #i.e. you have never observed ANY characters
        assert False    


    def probLastChar(self, gram : str) -> float:
    
            prefix=gram[:-1]
            prefixLen=len(prefix)
    
            total=0
            
            count = self.ngrams[prefixLen][gram]
            
            for c in self.chars:            
                total = total + self.ngrams[prefixLen][prefix+c]
    
            if count == 0:
                return self.probLastChar(gram[1:])
            else:
                return 1.0*count/total
            
    def logProbSeq(self, text, prevLen : int = 1):

         prob=0
         gi = self.gramIter(self.cleanIter(iter(text)),prevLen+1)

         for gram in gi:
             prob= prob + np.log2(self.probLastChar(gram))

         return prob
         
    '''
    Should be low if ngram model and the actual text agree
    '''
    def avgEntropy(self, text, prevLen : int =1):

        prob=0
        ccount=0
        gi = self.gramIter(self.cleanIter(iter(text)),prevLen+1)

        for gram in gi:
            ccount=ccount+1
            prob= prob + np.log2(self.probLastChar(gram))

        return -prob/ccount


    def substitute(self, orig : str, subs :str, text :str) -> str:
        outText = ''
        
        assert len(orig) == len(subs)
        
           
        subsDict=dict(zip(orig,subs))
     
    
        for c in self.cleanIter(iter(text)):
            
            if c in orig:
                outText = outText + subsDict[c]
            else:
                outText = outText + c
        return outText        


    def grow(self, text : str, gramLen : int = 4):
        '''
        Take an arbitrary lenght text and add one more character, using the 
        last gramLen characters.
        '''
        
        
        '''
        <<< YOUR CODE HERE >>>
        '''
        if gramLen==0 :
            return text+ self.nextChar('')
        return text +self.nextChar(text[-gramLen:])
        #return text + 'some character'
    
    def makeSentence(self, gramLen : int = 4):
        text=''
        '''
        <<YOUR CODE HERE>>>
        '''
        print('i am here')
        countPeriods = 0
        while countPeriods!=2: 
            text= self.grow(text, gramLen)
            # print(text, "this is text")
            if text[len(text)-1]=='.':
                countPeriods=countPeriods+1
        text = text.split(".",1)
        print(text)
        t = text[1]
        print(t)
        return t


    def decode(self, text : str):
        '''
        <<YOUR CODE HERE>>>
        '''

        return 'orig','subs'



if __name__ == '__main__':
        
    ng=Ngrams()
    ng.loadGrams('smallGrams.pkl')
    
    
    scrambledText  =  " xvkndui?d).xc,) nwwnxqv)x ?c,)wxvi" \
                 + ")xfjnw)nd)xd)?jwxdt?m)lwxbm)k?i,w) k,j" \
                 + ",)k,) xv)w,xtndu)x)ijxndndu)v,vvn?db)s" \
                 + "k,scndu)i nii,jm)qjb) nwwnxqvm)x)sy!,j" \
                 + "v,sojniy),hf,jim) xv)tnvqxy,t)i?)tnvs?" \
                 + "a,j)ikxi)k,)kxt)!,,d)ikjovi)ndi?)ik,)q" \
                 + "nttw,)?l)?d,)?l)ik,) ?jvi)v,sojniy)t,!" \
                 + "xsw,v),a,j)i?)!,lxww)xq,jnsxd)ndi,wwnu" \
                 + ",ds,b)qjb) nwwnxqv)kxt) jnii,d)?d)knv)" \
                 + "s?qfxdy)!w?u)x!?oi)ik,)vkxt? )!j?c,jvm" \
                 + ")x)qyvi,jn?ov)uj?of)ikxi)kxt)v?q,k? )?" \
                 + "!ixnd,t)qxdy)?l)ik,)kxscndu)i??wv)ik,)" \
                 + "odni,t)vixi,v)ov,t)i?)vfy)?d)?ik,j)s?o" \
                 + "dijn,vb)d? )ik,)uj?of)kxt)j,fwn,t)nd)x" \
                 + "d)xdujy)vsj,,t)?d)i nii,jb)ni)nt,dinln" \
                 + ",t)knq)s?jj,siwy)xv)x)l?jq,j)q,q!,j)?l" \
                 + ")ik,)dxin?dxw)v,sojniy)xu,dsyv)kxscndu" \
                 + ")uj?ofm)ixnw?j,t)xss,vv)?f,jxin?dvm)?j" \
                 + ")ibxb?bm)x).?!)k,)kxt)d?i)fo!wnswy)tnv" \
                 + "sw?v,tb)ik,d)ik,)vkxt? )!j?c,jv)xvi?dn" \
                 + "vk,t)knq)!y)tj?ffndu)i,skdnsxw)t,ixnwv" \
                 + ")ikxi)qxt,)sw,xj)ik,y)cd, )x!?oi)knukw" \
                 + "y)swxvvnln,t)kxscndu)?f,jxin?dv)ikxi)k" \
                 + ",)kxt)s?dtosi,tb)gik,y)kxt)?f,jxin?dxw" \
                 + ")ndvnuki)ikxi),a,d)q?vi)?l)qy)l,ww? )?" \
                 + "f,jxi?jv)xi)ibxb?b)tnt)d?i)kxa,mg)vxnt" \
                 + ")qjb) nwwnxqvm)d? ) nik)j,dtnin?d)ndl?" \
                 + "v,sm)x)sy!,jv,sojniy)lnjq)k,)l?odt,tb)" \
                 + "gn)l,wi)wnc,)nt)!,,d)cnsc,t)nd)ik,)uoi" \
                 + "b) k?,a,j) j?i,)iknv),nik,j) xv)x) ,ww" \
                 + "fwxs,t)ndvnt,j)?j)kxt)vi?w,d)x)w?i)?l)" \
                 + "?f,jxin?dxw)txixbg)ik,).?wi)i?)qjb) nw" \
                 + "wnxqv)lj?q)ik,)vkxt? )!j?c,jv)jnf?vi,)" \
                 + "xv)fxji)?l)x)qosk)!j?xt,j),xjik'oxc,)i" \
                 + "kxi)kxv)vkxc,d)ik,)dbvbxb)i?)niv)s?j,b" \
                 + ")sojj,di)xdt)l?jq,j)xu,dsy)?llnsnxwv)v" \
                 + "xy)ik,)vkxt? )!j?c,jv)tnvsw?voj,vm) kn" \
                 + "sk)!,uxd)nd)xouovi)m)kxa,)!,,d)sxixvij" \
                 + "?fkns)l?j)ik,)dbvbxbm)sxwwndu)ndi?)'o," \
                 + "vin?d)niv)x!nwniy)i?)fj?i,si)f?i,di)sy" \
                 + "!,j ,xf?dv)xdt)niv)a,jy)axwo,)i?)dxin?" \
                 + "dxw)v,sojniyb)ik,)xu,dsy)j,uxjt,t)xv)i" \
                 + "k,) ?jwtv)w,xt,j)nd)!j,xcndu)ndi?)xta," \
                 + "jvxjn,v)s?qfoi,j)d,i ?jcv)lxnw,t)i?)fj" \
                 + "?i,si)niv)? d"
    
    
    
    '''
    The two functions that do the heavy lifting are:
        nextChar(gram)
        probLastChar(gram)
        
    In both cases gram is a short sequence of characters, and nextChar
    tries to use the entire gram to predict the next character, based on the 
    entier gram. probLastChar returns the probability of the last character 
    given all but the last character.
    '''
    
    '''
    Draw a random charcter from the training set without prediciton, i.e. 
    use no characters to predicet the next one which gives you character
    statistics.
    '''

    someChar=ng.nextChar('')
    
    print("Drawing random character from training set using 'nextChar('')':" + someChar)
    print("The probability of that character can be calculated with 'probLastChar(" + someChar + ")':" + str(ng.probLastChar(someChar)))

    print("To compute the logProbability of whole sequence using the longest grams" +
          "possible, use 'logProbSeq()', less likely seuqnces will be more negative.\n\n")
    
    print("Log prob of 'Mice are great pets!'=" +  str(ng.logProbSeq('Mice are great pets.')) )
    print("Log prob of 'Mica zre gread bets!'=" + str(ng.logProbSeq('Mica zre gread bets.')) )
    
    '''
    Since the second one is not really english, it will have a lower probability, i.e. be 
    more negative. This works great to compare two strings of the same length, but you 
    can also normalize by the number of characters and see how 'surprising' the characters
    are on average given the statistical model of the grams (avgEntropy). If the characters come
    from the distribution, then they should be less surprising. For example, if you 
    used english statistics to copmute the probability of 
    "Informatik ist mein Lieblingsfach!" you should be surprised. 
    '''
        



    
    ''' 
    Some useage hints: If you want to rank characters in scrambled text you can do something like:
        
    '''  

    charCnt = Counter(scrambledText) #Way to count next characters

    charlist=charCnt.most_common()   #return a list of (char,cnt) 
                                     #pairs witht he most common
    
    # print(charlist)
    # cl=''
    # cl = [cl+ i[0] for i in charlist]
    # d=''
    # for x in cl:
    #     d=d+x
    # print(d)
    # print(cl)
    # c=ng.makeSentence()
    # # ng.substitute()
    # # whatever letter i wanted to swap i mdde sure it woulff work by printing it out a million times. 
    # print(ng.substitute(d, ' etaoirsnhldcwm.uygpbfk,v"jqx', scrambledText))# well this took forever very cool though 

    # print(c)
    # print(ng.substitute(ng.decode(), scrambledText))# well this took forever very cool though 
