function [status]=setparammmat3d(name, var, ni,nj,nk,nr,nc,elist)
  %AddMetadata(name, property, port) 
  
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

    ind=1;
    for i1=1:ni
       for i2=1:nj
          for i3=1:nk
            for i=1:nr
              for j=1:nc
               tmat(ind)=var(i1,i2,i3,i,j);
               ind=ind+1;
              end
            end
        end
      end
    end

  sval=vectostring(tmat',',');
  
  scommand=['iogs setparam mmat3d ',name,' ',sval,' ',num2str(ni),' ',num2str(nj),' ',num2str(nk),' ',num2str(nr),' ',num2str(nc),' ',num2str(id),' ',sport,' ',server];
  system(scommand); 

    %status=iosetparammat3d(obj, id,name,tmat,ni,nj,nk,nr,nc);

%endfunction


function status = iosetparammmat3d(obj,id,name,value,n,p,q,nr,nc)
%setparammmat3d(obj,id,name,value,n,p,q,nr,nc)
%
%   Service definition of function ns__setparammmat3d
%   
%     Input:
%       id = (int)
%       name = (string)
%       value = (Array)
%       n = (int)
%       p = (int)
%       q = (int)
%       nr = (int)
%       nc = (int)
%   
%     Output:
%       status = (int)

% Build up the argument lists.
values = { ...
   id, ...
   name, ...
   value, ...
   n, ...
   p, ...
   q, ...
   nr, ...
   nc, ...
   };
names = { ...
   'id', ...
   'name', ...
   'value', ...
   'n', ...
   'p', ...
   'q', ...
   'nr', ...
   'nc', ...
   };
types = { ...
   '{http://www.w3.org/2001/XMLSchema}int', ...
   '{http://www.w3.org/2001/XMLSchema}string', ...
   'Array', ...
   '{http://www.w3.org/2001/XMLSchema}int', ...
   '{http://www.w3.org/2001/XMLSchema}int', ...
   '{http://www.w3.org/2001/XMLSchema}int', ...
   '{http://www.w3.org/2001/XMLSchema}int', ...
   '{http://www.w3.org/2001/XMLSchema}int', ...
   };

% Create the message, make the call, and convert the response into a variable.
soapMessage = createSoapMessage( ...
    'urn:IoSteerWS', ...
    'setparammmat3d', ...
    values,names,types,'rpc');
response = callSoapService( ...
    obj.endpoint, ...
    '', ...
    soapMessage);
status = parseSoapResponse(response);
