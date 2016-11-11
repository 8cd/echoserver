import socket                                                                   
import os                                                                       
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                           
s.bind(('0.0.0.0',2222))                                                        
s.listen(1)                                                                     
for i in range(10):                                                             
        fid=os.fork()                                                           
        if fid==0:                                                              
                while True:                                                     
                        conn, addr = s.accept()                                 
                        while True:                                             
                                data = conn.recv(1024)                          
                                if (not data) or (data=='close'): break         
                                conn.send(data)                                 
                        conn.close()