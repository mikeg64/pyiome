function [value]=writelocalsimulation(filename,elist)
  %GetMetadata(name, property, port) 
  
  nargin=length(elist);
  if nargin>0
    server=elist{1};
    if nargin>1
      port=elist{2};
      if nargin>2
         id=elist{3};
      else
         id=0;
      end 
    else
      port=8080;
    end
  else
    server='localhost';
    port=8080;
    id=0;
  end

    sport=sprintf('%d',port);
  obj.endpoint=['http://',server,':',sport];



  value=iowritelocalsimulation(obj,id,filename);

	fid = fopen(filename,'w');
	fprintf(fid,'%s',value);
	
	status = fclose(fid);

  %return value;
  
 %endfunction



function filecontent = iowritelocalsimulation(obj,id,filename)
%writelocalsimulation(obj,id,filename)
%
%   Service definition of function ns__writelocalsimulation
%   
%     Input:
%       id = (int)
%       filename = (string)
%   
%     Output:
%       filecontent = (string)

% Build up the argument lists.
values = { ...
   id, ...
   filename, ...
   };
names = { ...
   'id', ...
   'filename', ...
   };
types = { ...
   '{http://www.w3.org/2001/XMLSchema}int', ...
   '{http://www.w3.org/2001/XMLSchema}string', ...
   };

% Create the message, make the call, and convert the response into a variable.
soapMessage = createSoapMessage( ...
    'urn:IoSteerWS', ...
    'writelocalsimulation', ...
    values,names,types,'rpc');
response = callSoapService( ...
    obj.endpoint, ...
    '', ...
    soapMessage);
filecontent = parseSoapResponse(response);
