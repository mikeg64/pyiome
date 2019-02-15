function [elist]=iome(server,port,id)
% set the iome elist variable using [elist]=iome(server,port,id)
% the elist cell array is used in subsequent calls to iome routines
%
% for example see 
% addparameter routines
% addparamdouble, addparamint, addparamvec,
% addparamstring,addparammat,addmetadata
% 
% getparameter routines
% getparamdouble, getparamint, getparamvec,
% getparamstring,getparammat,getmetadata
%
% set parameter routines
% setparamdouble, setparamint, setparamvec,
% setparamstring,setparammat,setmetadata
%
% general utilities
% listparam, deleteparam, listmetadata, deletemetadata
%
% job service submission and creation to be developed later



  if nargin>0 
    selist.server=server;
    if nargin>1 
      selist.port=port;
      if nargin>2 
         selist.id=id;
      else
         id=0;
      end 
    else
      port=8080;
    end
  else
    selist.server='localhost';
    selist.port=8080;
    selist.id=0;
  end

elist=struct2cell(selist);