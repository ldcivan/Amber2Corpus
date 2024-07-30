import json
import csv

character_name = '迪希雅'

# 读取JSON文件
with open(character_name + '.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 存储所有对话的列表
conversations = []

# 遍历指定路径
storyList = data['data']['storyList']
for storyList_key, storyList_value in storyList.items():
    print(f"Processing storyList {storyList_key}")
    story = storyList_value['story']
    for story_key, story_value in story.items():
        print(f"  Processing story {story_key}")
        taskData = story_value['taskData']
        try:
            for taskData_index, taskData_value in enumerate(taskData):
                print(f"    Processing taskData {taskData_index}")
                items = taskData_value['items']
                conversation = ''
                for item_key, item_value in items.items():
                    print(f"      Processing items {item_key}")
                    # 提取role和text
                    dialogue = []
                    role = item_value.get('role', '')
                    texts = item_value.get('text', [])
                    for text_entry in texts:
                        text = text_entry.get('text', '')
                        dialogue.append(f"{role}：{text}")
                    # 将对话内容合并为一个字符串
                    conversation += str(dialogue).replace('\']', '\n').replace('[\'', '')
                conversations.append(conversation)
        except KeyError as e:
            print(f"KeyError: {e}")
            continue
        except TypeError as e:
            print(f"TypeError: {e}")
            continue

# 将对话保存到CSV文件中
with open(character_name + '.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["序号", "对话"])  # 写入表头
    for i, conversation in enumerate(conversations, 1):
        csvwriter.writerow([i, conversation])

print("对话已保存到output.csv文件中。")
