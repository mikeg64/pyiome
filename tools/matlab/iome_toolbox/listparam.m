function [list]=listparam(type,elist)
  %[list]=listparam(type,elist)
  
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
  list=iolistparam(obj,type, id);
  %%return list;
  
 %endfunction





function list = iolistparam(obj,type,id)
%listparam(obj,type,id)
%
%   Service definition of function ns__listparam
%   
%     Input:
%       type = (string)
%       id = (int)
%   
%     Output:
%       list = (string)

% Build up the argument lists.
values = { ...
   type, ...
   id, ...
   };
names = { ...
   'type', ...
   'id', ...
   };
types = { ...
   '{http://www.w3.org/2001/XMLSchema}string', ...
   '{http://www.w3.org/2001/XMLSchema}int', ...
   };

% Create the message, make the call, and convert the response into a variable.
soapMessage = createSoapMessage( ...
    'urn:IoSteerWS', ...
    'listparam', ...
    values,names,types,'rpc');
response = callSoapService( ...
    obj.endpoint, ...
    '', ...
    soapMessage);
list = parseSoapResponse(response);
