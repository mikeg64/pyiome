function [isimid]=submitsimulation(simfile,elist)
  %GetMetadata(name, property, port) 
  
  nargin=length(elist);
  if nargin>0 then
    server=elist{1};
    if nargin>1 then
      port=elist{2};
      if nargin>2 then
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

  fid = fopen(filename, 'r');
  [a,count] = fscanf(fid, '%c', inf);
  fclose(fid);
  isimid=iosubmitsimulation(obj,id,a);
  %return isimid;
  
 %endfunction




function isimid = iosubmitsimulation(obj,simfilecontent)
%submitsimulation(obj,simfilecontent)
%
%   Service definition of function ns__submitsimulation
%   
%     Input:
%       simfilecontent = (string)
%   
%     Output:
%       isimid = (int)

% Build up the argument lists.
values = { ...
   simfilecontent, ...
   };
names = { ...
   'simfilecontent', ...
   };
types = { ...
   '{http://www.w3.org/2001/XMLSchema}string', ...
   };

% Create the message, make the call, and convert the response into a variable.
soapMessage = createSoapMessage( ...
    'urn:IoSteerWS', ...
    'submitsimulation', ...
    values,names,types,'rpc');
response = callSoapService( ...
    obj.endpoint, ...
    '', ...
    soapMessage);
isimid = parseSoapResponse(response);
