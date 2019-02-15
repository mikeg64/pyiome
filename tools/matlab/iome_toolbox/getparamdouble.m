function [value]=getparamdouble(name,elist)
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
  value=str2num(iogetparamdouble(obj,id,name));
  %return value;
  
 %endfunction


function value = iogetparamdouble(obj,id,name)
%getparamdouble(obj,id,name)
%
%   Service definition of function ns__getparamdouble
%   
%     Input:
%       id = (int)
%       name = (string)
%   
%     Output:
%       value = (double)

% Build up the argument lists.
values = { ...
   id, ...
   name, ...
   };
names = { ...
   'id', ...
   'name', ...
   };
types = { ...
   '{http://www.w3.org/2001/XMLSchema}int', ...
   '{http://www.w3.org/2001/XMLSchema}string', ...
   };

% Create the message, make the call, and convert the response into a variable.
soapMessage = createSoapMessage( ...
    'urn:IoSteerWS', ...
    'getparamdouble', ...
    values,names,types,'rpc');
response = callSoapService( ...
    obj.endpoint, ...
    '', ...
    soapMessage);
value = parseSoapResponse(response);
