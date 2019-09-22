'''
@description 2019/09/22 14:07
'''

# 2.把有病毒的文件修改为正常的代码。
# 病毒文件为：virus.html

lines = []
with open('virus.html', 'r', encoding='utf-8') as fp:
    is_virus = False
    for line in fp:
        if line.find('<script type="text/javascript">') > -1:
            is_virus = True
        elif line.find('</script>') > -1:
            is_virus = False
        else:
            if not is_virus: # 不处于病毒代码中
                lines.append(line)

with open('virus_repair.html', 'w', encoding='utf-8') as fp:
    fp.writelines(lines)