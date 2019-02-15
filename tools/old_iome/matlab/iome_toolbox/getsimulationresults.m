function [result]=getsimulationresults(outfile, elist)
%function [status]=InitIOME(simname, configname, statename,port,server)
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
  %Submit the generic simulation
  %Simulation Config name
  %returns
  
  
  result=iogetsimulationresults(obj,isimid);
  
%endfunction


function result = iogetsimulationresults(obj,isimid)
%getsimulationresults(obj,isimid)
%
%   Service definition of function ns__getsimulationresults
%   
%     Input:
%       isimid = (int)
%   
%     Output:
%       result = (string)

% Build up the argument lists.
values = { ...
   isimid, ...
   };
names = { ...
   'isimid', ...
   };
types = { ...
   '{http://www.w3.org/2001/XMLSchema}int', ...
   };

% Create the message, make the call, and convert the response into a variable.
soapMessage = createSoapMessage( ...
    'urn:IoSteerWS', ...
    'getsimulationresults', ...
    values,names,types,'rpc');
response = callSoapService( ...
    obj.endpoint, ...
    '', ...
    soapMessage);
result = parseSoapResponse(response);
