#!/usr/bin/env python
# coding: utf-8

# In[94]:


import streamlit as st


# In[95]:


a = int(st.text_input('length1',345))
b = int(st.text_input('length2',348))
c = int(st.text_input('breadth1',360))
d = int(st.text_input('breadth2',364))


# In[96]:


l = range(a,b)
b = range(c,d)


# In[97]:


aya_mul = 9
aya_div = 8
vara_mul = 9
vara_div = 7
amsha_mul = 6
amsha_div = 9
dravya_mul = 8
dravya_div = 12
runa_mul = 3
runa_div = 8
tidhi_mul = 8
tidhi_div = 30
yoga_mul = 4
yoga_div = 27
ayu_mul = 8
ayu_div = 120


# In[105]:


for m in l:
    for n in b: 
        if ((m*n)*aya_mul) % aya_div == 0:
            ayam = aya_div
        else:
            ayam = ((m*n)*aya_mul) % aya_div
        if ((m*n)*vara_mul) % vara_div == 0:
            varam = vara_div
        else:
            varam = ((m*n)*vara_mul) % vara_div
        if ((m*n)*amsha_mul) % amsha_div == 0:
            amsham = amsha_div
        else:
            amsham = ((m*n)*amsha_mul) % amsha_div
        if ((m*n)*dravya_mul) % dravya_div == 0:
            dravyam = dravya_div
        else:
            dravyam = ((m*n)*dravya_mul) % dravya_div
        if ((m*n)*runa_mul) % runa_div == 0:
            runam = runa_div
        else:
            runam = ((m*n)*runa_mul) % runa_div
        if ((m*n)*tidhi_mul) % tidhi_div == 0:
            tidhi = tidhi_div
        else:
            tidhi = ((m*n)*tidhi_mul) % tidhi_div
        if ((m*n)*yoga_mul) % yoga_div == 0:
            yogam = yoga_div
        else:
            yogam = ((m*n)*yoga_mul) % yoga_div
        if ((m*n)*ayu_mul) % ayu_div == 0:
            ayu = ayu_div
        else:
            ayu = ((m*n)*ayu_mul) % ayu_div
        if (ayam not in [2,4,6,8])         & (varam not in [1,3,7])         & (amsham not in [1,3,4,6,8])         & (dravyam > runam)         & (tidhi not in [4,9,14,19,24,29,30])         & (yogam not in [1,6,9,13,15,17,19,27]):
            st.write('Length: ',m,'\nBreadth: ',n)
            st.write('\nAyam: ',ayam)
            st.write('\nVaram: ',varam)
            st.write('\nAmsham: ',amsham)
            st.write('\nDravyam: ',dravyam)
            st.write('\nRunam: ',runam)
            st.write('\nTidhi: ',tidhi)
            st.write('\nYogam: ',yogam)
            st.write('\nAayushu: ',ayu)

