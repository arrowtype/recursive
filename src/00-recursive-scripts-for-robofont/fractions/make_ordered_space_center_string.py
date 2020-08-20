"""
    To print out a nice string for the space center.
"""

sups = "zerosuperior onesuperior twosuperior threesuperior foursuperior \
        fivesuperior sixsuperior sixsuperior.ss01 sevensuperior eightsuperior \
        ninesuperior ninesuperior.ss01 \
        zerosuperior.slash zerosuperior.dotted zerosuperior.sans \
        zerosuperior.afrc onesuperior.afrc twosuperior.afrc threesuperior.afrc \
        foursuperior.afrc fivesuperior.afrc sixsuperior.afrc sixsuperiorss01.afrc \
        sevensuperior.afrc eightsuperior.afrc ninesuperior.afrc ninesuperiorss01.afrc  \
        zerosuperiorslash.afrc zerosuperiordotted.afrc zerosuperiorsans.afrc".split()

print(len(sups))

# # Use with control character between, sorted
# for i, sup in enumerate(sups):
#     if i != 0 and i % 5 == 0:
#         print("\\n", end="")

#     print(f"/{sup}/{sup.replace('superior','inferior')}", end=" ")

#     if i == len(sups) - 1:
#         print("/zerowidthspace")

# # With fraction.split between, sorted
# for i, sup in enumerate(sups):
#     if i != 0 and i % 5 == 0:
#         print("\\n", end="")

#     print(f"/{sup}/fraction.split/{sup.replace('superior','inferior')}", end=" ")

#     if i == len(sups) - 1:
#         print("/zerowidthspace")

for i, sup in enumerate(sups):
    print(f"/{sup}", end=" ")

for i, sup in enumerate(sups):
    print(f"/{sup.replace('superior','inferior')}", end=" ")

    if i == len(sups) - 1:
        print("/zerowidthspace")