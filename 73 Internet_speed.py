import speedtest
st=speedtest.Speedtest()
download=st.download()
upload=st.upload()
download=download/1000000
upload=upload/1000000

print("Your download speed is",round(download,3),'Mbps')
print("Your upload speed is",round(upload,3),'Mbps')

st.get_servers([])
ping=st.results.ping
print("your ping is",ping)