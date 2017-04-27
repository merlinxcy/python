import iptc
import os
#os.system("export PATH=$PATH:/root/File/Programe/Python/iptables/iptcFirewall")#按照不同系统初始化环境变量
#os.system("export PATH=$PATH:/root/File/Programe/Python/iptables")
from lib.utils import check_string,display

class ShowIptables:

  debug=False#debug开启会出现调试信息，debug关闭不会出现调试信息

  def __init__(self,debug=False):
    self.debug=debug

  def check_table(self,table_name):
    try:
      if not check_string(table_name):
       raise Exception("[-] Table name is not a string or unicode")
      if iptc.is_table_available(table_name):#调用iptc库判别table名字是否合法,源码在ip2tc.py中
       return True
      return False
    except Exception as e:
      if self.debug:
        display(str(e))
      return False

  def check_chain(self,table_name,chain_name):
    try:
      if not check_string(chain_name):
        raise Exception("[-] Chain name is not a string or unicode")
      if not self.check_table(table_name):
        raise Exception("[-] Table name is illegal")
      table=iptc.Table(table_name)#将iptables中的表赋值给table
      return table.is_chain(chain_name)#调用table对象中的is_chain默认函数
    except Exception as e:
      if self.debug:
        display(str(e))
      return False

  def show_chains(self,table_name):
    try:
      if not self.check_table(table_name):
        raise Exception("[-] Table name is illegal")
        table=iptc.Table(table_name)
        chains=[]
        for chain in table.chains:
          chains.append(chain)#将iptables系统table中所有的chain加入chains
        return chains
    except Exception as e:
      if self.debug:
        display(str(e))
      return None

  def get_rules(self,table_name,chain_name):
    try:
        if not self.check_table(table_name):
          raise Exception("[-] Table name is illegal")
        table=iptc.Table(table_name)
        if not self.check_chain(table_name,chain_name):
          raise Exception("[-] Chain name is illegal")
        chain=iptc.Chain(table,chain_name)#在表中提取具体名字的链
        rules=chain.__get_rules()
        return rules
    except Exception as e:
        if self.debug:
          display(str(e))
        return None

  def display(self,table_name,chain_name):
    display("display"+table_name+" "+chain_name)
    try:
      if not self.check_table(table_name):
        raise Exception("[-] Table name is illegal")
      table=iptc.Table(table_name)
      if not self.check_chain(table_name,chain_name):
        raise Exception("[-] Chain name is illegal")
      chain=iptc.Chain(table,chain_name)
      rules=chain._get_rules()#从链表中获取rule规则
      for rule_number in range(len(rules)):
        rule=rules[rule_number]
        print "------------------------------------------------"
        print rule_number," #protocol: ",rule.protocol," #src: ",rule.src," #dst: ",rule.dst
        if len(rule.matches)>0:#再从rule中读取匹配
          print "Matches:"
          for match in rule.matches:
              if match.sport:
                print "sport:  ",match.sport
              if match.dport:
                print "dport:  ",match,dport
        print "Action:"
        print rule.target.name
    except Exception as e:
      if self.debug:
        display(str(e))
      return None









class SetIptables:

  debug=False
  method=""
  table_name=None
  chain_name=None
  method_list=["add","delete"]
  add_or_insert_rule_dict={}
  action_list=["ACCEPT","DROP","REJECT"]
  protocol_list=["tcp","udp","icmp"]
  success=False
  error_message=""

  def __init__(self,debug=False,table_name="",chain_name="",method="",rule_dict={}):
    display("set iptables "+table_name+"  "+chain_name+"  "+method+"  "+str(rule_dict))
    self.debug=debug
    if check_string(table_name) and check_string(chain_name) and check_string(method):
      self.table_name=table_name
      self.chain_name=chain_name
      self.method=method
      if rule_dict: #如果初始化的rule_dict不是NONE的话就用其初始化
        self.add_or_insert_rule_dict=rule_dict
        if self.make_rule():
          self.success=True
      else:
        if self.debug:
          display("illagel string")

  def successful(self):
    return self.success

  def _table_and_chain_check(self):
    checker=ShowIptables()  #构造之前定义的ShowIptables的对象
    if not checker.check_table(self.table_name):
      self.error_message="table not found"
      return False
    if not checker.check_chain(self.table_name,self.chain_name):
      self.error_message="chain not found"
      return False
    return True

  def _method_check(self):
    if self.method in self.method_list:
      return True
    return False

  def make_rule(self):
    if not self._method_check():
      return False
    if not self._table_and_chain_check():
      return False
    if self.method=="add":
      return self.add_rule()
    elif self.method=="delete":
      return self.delete_rules()
    else:
      return

  def add_rule(self):
    try:
      chain=iptc.Chain(iptc.Table(self.table_name),self.chain_name)
      rule=iptc.Rule()#创建空rule
              #从add-or_insert_rule_dict中获取参数
      if self.add_or_insert_rule_dict.get("aciton") and self.add_or_insert_rule_dict.get("action","") in self.action_list:
        rule.target=rule.create_target(self.add_or_insert_rule_dict.get("action"))
      else:
        return False
      if self.add_or_insert_rule_dict.get("sip",""):
        rule.set_src(self.add_or_insert_rule_dict.get("sip"))#iptc的set_src方法

      if self.add_or_insert_rule_dict.get("dip",""):
        rule.set_dst(self.add_or_insert_rule_dict.get("dip"))#set_dst方法

      if self.add_or_insert_rule_dict.get("iintf",""):
        rule.set_in_interface(self.add_or_insert_rule_dict.get("iintf"))

      if self.add_or_insert_rule_dict.get("ointf",""):
        rule.set_out_interface(self.add_or_insert_rule_dict.get("ointf"))

      if self.add_or_insert_rule_dict.get("protocol",""):
        if self.add_or_insert_rule_dict.get("protocol","") in self.protocol_list:
          rule.set_protocol(self.add_or_insert_rule_dict.get("protocol"))
        else:
          self.error_message="[-] unkown protocol"
          return False
      dport=self.add_or_insert_rule_dict.get("dport","")
      sport=self.add_or_insert_rule_dict.get("sport","")
      if dport or sport:
        if not self.add_or_insert_rule_dict.get("protocol",""):
          self.error_message="[-] no protocol"
          return False
        match=rule.create_match("tcp")
        print match
        if dport:
          match.dport=dport
        if sport:
          match.sport=sport
      chain.insert_rule(rule)
      self.error_message=""
      return True
    except Exception as error:
      self.error_message="[-] "+str(error)
      if self.debug:
        display(self.error_message)
    return False


  def insert_rules(self):
    pass


  def delete_rules(self):
    try:
      chain=iptc.Chain(iptc.Table(self.table_name),self.chain_name)
      if self.add_or_insert_rule_dict.get("number","")=="all":
        for rule in chain._get_rules():
          chain.delete_rule(rule)
          self.error_message=""
          return True
      else:
        num=int(self.add_or_insert_rule_dict.get("number",""))
        if not isinstance(num,int)
          return False
        for rule_num in range(len(chain._get_rules()):
          if rule_num==num:
            chain.delete_rule(chain.rules[rule_num])
            break
          self.error_message=""
          return True
    except Exception as e:
      self.error_message="[-] "+str(error)
      if self.debug:
        display(self.error_message)
    return False




































