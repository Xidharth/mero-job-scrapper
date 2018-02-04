
# coding: utf-8 Wrote while learning web scrapping

# In[1]:


import requests
import csv


# In[2]:


from bs4 import BeautifulSoup


# In[15]:


myFile = open('example2.csv', 'w')
writer = csv.writer(myFile)


# In[4]:



headerList=[]
bodylist=[]


# In[5]:


payload={'Keywords':'developer'} #change this to as per your query


# In[6]:


page = requests.post('http://www.jobsnepal.com/simple-job-search',data=payload)


# In[7]:


soup = BeautifulSoup(page.text, 'html.parser')


# In[8]:


table=soup.find("table", {"class":"gridx"})


# In[9]:


tableheadrow=table.find('tr').find_all('th')


# In[16]:


for row in tableheadrow:
    headerList.append(row.find('a').getText())
print(headerList)
writer.writerow(headerList)

    
    
    


# In[12]:


tablebody=table.find_all('tr')[1:]


# In[13]:


for row in tablebody:
    bodylist.append(row.find_all('td')[0].find('a').getText().replace('\t','').replace('\n',''))
    bodylist.append(row.find_all('td')[1].find('a').getText().replace('\t','').replace('\n',''))
    bodylist.append(row.find_all('td')[2].getText().replace('\t','').replace('\n',''))
    bodylist.append(row.find_all('td')[3].find('span').getText().replace('\t','').replace('\n',''))
    writer.writerow(bodylist)
    bodylist=[]
print('finished')
   
    
   
 




