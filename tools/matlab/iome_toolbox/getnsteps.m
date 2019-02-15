function [nsstep]=getnsteps(elist)
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
  nsstep=iogetnsteps(obj,id);
  %return nsstep;
  
 %endfunction



function nsstep = iogetnsteps(obj,id)
%getnsteps(obj,id)
%
%   Service definition of function ns__getnsteps
%   
%     Input:
%       id = (int)
%   
%     Output:
%       nsstep = (int)

% Build up the argument lists.
values = { ...
   id, ...
   };
names = { ...
   'id', ...
   };
types = { ...
   '{http://www.w3.org/2001/XMLSchema}int', ...
   };

% Create the message, make the call, and convert the response into a variable.
soapMessage = createSoapMessage( ...
    'urn:IoSteerWS', ...
    'getnsteps', ...
    values,names,types,'rpc');
response = callSoapService( ...
    obj.endpoint, ...
    '', ...
    soapMessage);
nsstep = parseSoapResponse(response);
