#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html><head><title>Bash as CGI"
echo "</title></head><body>"


echo "<b>NGINX_ADDR:</b>" $REMOTE_ADDR
echo "<b>NGINX_PORT:</b>" $REMOTE_PORT
echo "<b>CLIENT_ADDR:</b> " $HTTP_X_REAL_IP
echo "<b>CLIENT_PORT:</b> " $HTTP_X_FORWARDER_FOR_PORT
echo "<b>NGINX_VERSION:</b>" $HTTP_X_NGX_VERSION

echo "<h1>Load Average</h1>"
echo "$(cat /proc/loadavg | awk '{print $1" "$2" "$3}')"

echo "<h1>CPU</h1>"
echo "<pre>----- Usr+nice ------------ sys ---------- idle ---------- iowait</pre>" 
echo "<pre>$(cat /var/log/mpstat.log|tail -n 1 | awk '{printf("%15f %15s %15s %15s \n",$3+$4, $5, $12, $6)}')</pre>"

echo "<h1>Disk and Inodes info</h1>"
echo "<pre>----- File system ---- %Free space ---- Free space --- %Free inodes --  Free inodes</pre>"  
echo "<pre>$(cat /var/log/df.log| grep -v /dev* |grep -v /proc* |grep -v /sys*  | awk ' NR>1 {printf("%15s %15s %15s %15s %15s \n",$1,(100-$2),$3,(100-$4),$5)}')</pre>"

echo "<h1>TCP connection</h1>"
echo "<pre>$(cat /var/log/tcp.log)</pre>"

echo "<h1>UDP connection</h1>"
echo "<pre>$(cat /var/log/udp.log)</pre>"

echo "<h1>Network Loading</h1>"
echo "<pre>---- inteface --- bytes_recived --- packet_recived --- bytes_transmit --- packet_transmit</pre>"  
echo "<pre>$(cat /var/log/network | awk '  {printf("%15s %15s %15s %15s %15s \n",$1,$2,$3,$10,$11)}')</pre>"

echo "<h1>TCP connection status</h1>"
echo "<pre> ESTABLISHED $(netstat | grep EST | wc -l )</pre>"

echo "<h1>Load Disks</h1>"
echo "<pre> -------- Device ---------- r/s ---------- w/s ---------- await ---------- %util</pre>"
echo "<pre>$(cat /var/log/iostat.log | tail -n 3 |awk ' {printf("%15s %15s %15s %15s %15s \n",$1, $4, $5, $10, $14)}')</pre>" 

echo "</body></html>"


