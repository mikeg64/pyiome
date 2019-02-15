function [value]=getparamvec(name,n,elist)
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
  %value=iogetparamvec(name, n,obj,id);
  
 dval=iogetparamvec(obj,id,name,n);

value=cellarray2vec(dval);


  

  %return value;
  
 %endfunction



function dval = iogetparamvec(obj,id,name,n)
%getparamvec(obj,id,name,n)
%
%   Service definition of function ns__getparamvec
%   
%     Input:
%       id = (int)
%       name = (string)
%       n = (int)
%   
%     Output:
%       dval = (Array)

% Build up the argument lists.
values = { ...
   id, ...
   name, ...
   n, ...
   };
names = { ...
   'id', ...
   'name', ...
   'n', ...
   };
types = { ...
   '{http://www.w3.org/2001/XMLSchema}int', ...
   '{http://www.w3.org/2001/XMLSchema}string', ...
   '{http://www.w3.org/2001/XMLSchema}int', ...
   };

% Create the message, make the call, and convert the response into a variable.
soapMessage = createSoapMessage( ...
    'urn:IoSteerWS', ...
    'getparamvec', ...
    values,names,types,'rpc');
response = callSoapService( ...
    obj.endpoint, ...
    '', ...
    soapMessage);
dval = parseSoapResponse(response);
