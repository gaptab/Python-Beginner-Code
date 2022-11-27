import requests

status_dict={'Website':'Status'}

def main():
    with open('websites.txt','r') as fr:
        for line in fr:
            website=line.strip()
            status=requests.get(website).status_code
            status_dict[website]='working' if status==200 \
                else 'not working'
                
    print(status_dict)
    
if __name__=='__main__':
    main()