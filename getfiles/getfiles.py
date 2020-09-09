import wget

print('download with wget')

# url = 'https://annarchive.com/files/Drmg042.pdf'
# wget.download(url, '/Users/cjs/Downloads/test042.pdf')

for i in range(250,300):
    url = 'https://annarchive.com/files/Drmg'+i.__str__()+'.pdf'
    print('downloading '+url)
    wget.download(url)
print('fin')
