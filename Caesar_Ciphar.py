{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Caesar_cipher:\n",
    "    #adding parameter A---string, shift---how many letter to move\n",
    "    #we will need them everywhere\n",
    "    #so A,B,C,..... to 0,1,2,...\n",
    "    #let's test each class module\n",
    "    #m object is created\n",
    "    #oops\n",
    "    #the shift is circular.So After Z, comes A.Otherwise ord returns garbage.\n",
    "    #''.join----['A','B','C'] to 'ABC'\n",
    "    #','.join--- to 'A,B,C'\n",
    "    #we had ascii overloaded\n",
    "    #decryption is just opposite\n",
    "    #let's reload\n",
    "    #decrypt was actually right \n",
    "    #I did not use encrypted message there\n",
    "    def __init__(self,A,shift):\n",
    "        self.A=A\n",
    "        self.shift=shift\n",
    "        \n",
    "    def toNumeric(self):\n",
    "        N=[]\n",
    "        for i in self.A:\n",
    "            v=ord(i)-ord('A')\n",
    "            N.append(v)\n",
    "        return N\n",
    "    def Encrypt(self):\n",
    "        s=self.toNumeric()\n",
    "        t=[]\n",
    "        for i in s:\n",
    "            u=((i+self.shift)%26)\n",
    "            w=chr(u+ord('A'))\n",
    "            t.append(w)\n",
    "        v=''.join(t)\n",
    "        return v\n",
    "    def deCrypt(self):\n",
    "        s=self.toNumeric()\n",
    "        t=[]\n",
    "        for i in s:\n",
    "            u=((i-self.shift)%26)\n",
    "            w=chr(u+ord('A'))\n",
    "            t.append(w)\n",
    "        v=''.join(t)\n",
    "        return v\n",
    "            \n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[7, 4, 11, 11, 14, 25]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "m=Caesar_cipher(\"HELLOZ\",3)\n",
    "m.toNumeric()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'KHOORC'"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "m.Encrypt()\n",
    "#notice here"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'EBIILW'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "m.deCrypt()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "n=m.Encrypt()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<__main__.Caesar_cipher at 0x7febb41caf60>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "m"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "p=Caesar_cipher(\"KHOORC\",3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'HELLOZ'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p.deCrypt()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "#so here is our caesar ciphar code.Thanks for watching."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
