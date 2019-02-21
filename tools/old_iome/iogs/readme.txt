Original iome server code for linux

To run iogs set the PATH to the bin folder here and the LD_LIBRARY_PATH to the lib folder
To show dependencies
ldd iogs  

Start IOME server using
iogs initiome null $IOME_SIMNAME null  &

iogs readsimulation simfile.xml 0 $IOME_WSPORT localhost


