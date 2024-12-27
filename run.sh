cd 
source Códigos_VSC/Python/Ambiente/bin/activate
cd Códigos_VSC/Python/Redes/Sockets

if [ $1 = 'sUdp' ]; then
    python3 serverUdp.py; 
    exit 0;
elif [ $1 = 'cUdp' ]; then
    python3 clienteUdp.py; 
    exit 0;
elif [ $1 = 'sTcp' ]; then
    python3 serverTcp.py; 
    exit 0;
elif [ $1 = 'cd' ]; then
    python3 clienteDesafio.py; 
    exit 0;
elif [ $1 = 'sd' ]; then
    python3 serverDesafio.py; 
    exit 0;
else
    python3 clienteTcp.py; 
    exit 0;
fi

