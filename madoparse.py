import struct
import sys

saveInput = sys.argv[1];

with open(saveInput, "rb") as f:
    data = f.read()

# unpack all ints (big-endian, 4 bytes each)
num_ints = len(data) // 4
ints = struct.unpack(f"<{num_ints}i", data)

print("continueStage: ", ints[1])
print("continueDifficulty: ", ints[2])
print("continueScore: ", ints[3])
print("continueTime: ", ints[4])

# ---- Arrays ----
index = 5

for i in range(3):
    print(f"\nDifficulty {i}: ")
    for j in range(10):
        bestScore = ints[index]
        bestTime  = ints[index + 1]
        bestRank  = ints[index + 2]

        print(
            f"Level {j}: "
            f"bestScore={bestScore}, "
            f"bestTime={bestTime}, "
            f"bestRank={bestRank}"
        )
        index += 3
