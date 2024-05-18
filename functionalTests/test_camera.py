#rpicam-vid --level 4.2 -n -t 0 --width 1296 --height 972 --framerate 30 --inline -o - | cvlc stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/stream1}' :demux=h264
