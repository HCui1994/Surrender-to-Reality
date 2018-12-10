import glob
src_files = glob.glob("./吾心吾行澄如明镜所作所为皆属正义/*.py")
total_tags = [src_file.split("/")[2][:4] for src_file in src_files]
total_tags = set(total_tags)
archive_filenem = "./有痛苦才会有喜悦.md"
archived_tags = set()
with open(archive_filenem) as archive:
    entry = archive.readline()
    count = 0
    while entry:
        tag = entry[2:6]
        if not tag or tag[0] != '0':
            # print(tag)
            entry = archive.readline()
            continue
        archived_tags.add(tag)
        entry = archive.readline()
print("not archived:")
print(total_tags - archived_tags)