# -- coding: utf-8 --
import jsonrpc
from simplejson import loads
from socket import error as SocketError
import errno
from corenlp import StanfordCoreNLP
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
corenlp_dir = "stanford-corenlp-full-2014-08-27/"
#server = jsonrpc.ServerProxy(jsonrpc.JsonRpc20(),jsonrpc.TransportTcpIp(addr=("127.0.0.1", 8080),timeout=200.0))
server = StanfordCoreNLP(corenlp_dir)

orig_file = open('pubmed_1000.csv', 'r')
new_file = open('coref-1000.csv', 'w')
count = 0
gotdata = 1
result = []
for line in orig_file.readlines():
    cols = line.split('\t')
    message =  cols[2]

    simplemessage = "Stanford University is located in California. It is a great university."
    print "Sending line: " + str(count)
    data = server.parse(message)
    '''
    while not gotdata:
        try:
            print "Sending line: " + str(count)
            data = server.parse(message)
            gotdata = 1
        except:
            print "The connection got reseted."       
            break
    '''
    result = loads(data)
    #gotdata = 0
    if 'coref' in result.keys():
        for coref in result['coref']:
            for one in coref:
                pronoun_len = one[0][4] - one[0][3]
                noun_len = one[1][4] - one[1][3]
                build_noun = ''

                for i in range(one[1][3],one[1][4]):
                    if i == one[1][4]-1:
                        try:
                            build_noun += result['sentences'][one[1][1]]['words'][i][1]['Lemma']
                        except:
                            print "Problem with index: " + str(i) + "\n"
                            pass
                    else:           
                        build_noun += result['sentences'][one[1][1]]['words'][i][1]['Lemma'] + ' '

                for i in range(one[0][3],one[0][4]):
                    if i == one[0][4]-1:
                        result['sentences'][one[0][1]]['words'][i][1]['Lemma'] = build_noun
                    else:
                        result['sentences'][one[0][1]]['words'][i][1]['Lemma'] = ''


        output = ''    
        for words in result['sentences']:
            #for one in words['words']:
            for i in range(0,len(words['words'])):
                if i == len(words['words']) - 2:
                    if words['words'][i][1]['Lemma']:
                        output += words['words'][i][1]['Lemma']
                else:
                    if words['words'][i][1]['Lemma']:
                        output += words['words'][i][1]['Lemma'] + ' '
            new_file.write(output)
            #print output
            output = ''
        new_file.write('\n')
    count += 1
orig_file.close()
new_file.close()