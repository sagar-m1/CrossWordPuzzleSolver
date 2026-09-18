import random
import time
import os


WORDS_3 = [
    "CAT", "ARE", "TEN", "BAT", "ATE", "TEA", "DOG", "ONE", "GET", "NOT",
    "TOP", "POT", "TIP", "PIT", "PIN", "NIP", "PEN", "NET", "SET", "SIT",
    "FIT", "FAT", "FAR", "RAT", "TAR", "ART", "ARM", "RAM", "RAN", "RUN",
    "SUN", "SON", "SUM", "MAN", "MAP", "CAP", "CUP", "CUT", "HUT", "HOT",
    "HAT", "HIT", "HIS", "HIM", "HER", "HEN", "HEM", "BED", "RED", "LED",
    "FED", "BAD", "DAD", "MAD", "SAD", "PAD", "POD", "ROD", "GOD", "ROW",
    "BOW", "COW", "HOW", "NOW", "LOW", "LAW", "RAW", "SAW", "DAY", "MAY",
    "BAY", "RAY", "SAY", "PAY", "WAY", "KEY", "BOY", "TOY", "JOY", "BUY",
    "GUY", "DRY", "FLY", "CRY", "TRY", "SPY", "SKY", "SEA", "PEA", "BEE",
    "SEE", "FEE", "PIE", "TIE", "LIE", "DIE", "EGG", "ICE", "AGE", "AIR",
    "EAR", "OAK", "OWL", "OIL", "ANT", "APE", "AXE", "FOX", "BOX", "SIX",
    "BUS", "CAR", "CAB", "VAN", "JET", "ZIP", "WIN", "WON", "WAR", "WEB",
    "WET", "YAM", "YES", "YET", "ZOO", "YAW", "AGO", "MEN", "TED", "BAR",
    "DIG", "WAT", "MAR"
]

WORDS_4 = [
    "SWAN", "WIRE", "IDEA", "MEAT", "SWIM", "WIDE", "AREA", "NEAT", "CARD", "REAR",
    "DART", "LACE", "ACID", "CAVE", "EDEN", "BATS", "TEAM", "SAME", "TRIP", "ROPE",
    "IPSO", "PEST", "MINT", "TATE", "POST", "OGRE", "STAR", "TERM", "GAME", "EATS",
    "COLD", "LEAD", "DEER", "CHAT", "HOSE", "ASIA", "TEAR", "FLAG", "LANE", "ANNA",
    "GEAR", "EDGE", "AGUE", "TIME", "AMEN", "RENT", "TALK", "LEAN", "KANG", "WARM",
    "MARK", "BEAR", "EACH", "ACRE", "RHEA", "LION", "INTO", "OTTO", "NOON", "CAME",
    "MRET", "EETS", "HEAR", "EASE", "REAL", "BOAT", "ARID", "TEDE", "PART", "TART",
    "SALT", "TANG", "NEST", "EVER", "SEMI", "DARK", "KARK", "MAST", "ACHE", "SCAN",
    "TENT", "ROSE", "OPAL", "SAID", "ELDE", "BAKE", "BALL", "BAND", "BANK", "BARE",
    "BARK", "BARN", "BASE", "BATH", "BEAM", "BEAN", "BEAT", "BEEF", "BEER", "BELL",
    "BELT", "BEND", "BEST", "BIRD", "BITE", "BLOW", "BLUE", "BODY", "BOIL", "BOLD",
    "BOLT", "BOND", "BONE", "BOOK", "BOOM", "BOOT", "BORE", "BORN", "BOSS", "BOTH",
    "BOWL", "BULK", "BULL", "BURN", "BUSH", "BUSY", "CAFE", "CAKE", "CALM", "CAMP",
    "CANE", "CAPE", "CART", "CASE", "CASH", "CAST", "CELL", "CHEF", "CHIN", "CHIP",
    "CITY", "CLAP", "CLAY", "CLIP", "CLUB", "COAL", "COAT", "CODE", "COIN", "COME",
    "COOK", "COOL", "COPE", "COPY", "CORD", "CORE", "CORN", "COST", "CRAB", "CREW",
    "CROP", "CROW", "CURE", "CURL", "DASH", "DATA", "DATE", "DAWN", "DEAD", "DEAF",
    "DEAL", "DECK", "DEED", "DEEP", "DESK", "DIET", "DIRT", "DISC", "DISH", "DISK",
    "DOCK", "DOLL", "DOOM", "DOOR", "DOSE", "DOWN", "DRAW", "DROP", "DRUG", "DRUM",
    "DUCK", "DUST", "DUTY", "EARL", "EARN", "EAST", "EASY", "EVEN", "EVIL", "EXAM",
    "EXIT", "EYES", "FACE", "FACT", "FADE", "FAIL", "FAIR", "FALL", "FAME", "FARM",
    "FAST", "FATE", "FEAR", "FEAT", "FEED", "FEEL", "FEET", "FILE", "FILL", "FILM",
    "FIND", "FINE", "FIRE", "FIRM", "FISH", "FIST", "FLAT", "FLAW", "FLEA", "FLEE",
    "FLEW", "FLOW", "FOAM", "FOIL", "FOLD", "FOLK", "FOOD", "FOOL", "FOOT", "FORK",
    "FORM", "FORT", "FOUR", "FREE", "FROG", "FROM", "FUEL", "FULL", "FUND", "GAIN",
    "GATE", "GIFT", "GIRL", "GIVE", "GLAD", "GLOW", "GOAL", "GOAT", "GOLD", "GOLF",
    "GOOD", "GRAB", "GRID", "GROW", "HAIR", "HALF", "HALL", "HALT", "HAND", "HANG",
    "HARD", "HARM", "HATE", "HAVE", "HAWK", "HEAD", "HEAL", "HEAT", "HEEL", "HELP",
    "HERB", "HERD", "HERO", "HIDE", "HIGH", "HILL", "HINT", "HIRE", "HOLD", "HOLE",
    "HOME", "HOOK", "HOPE", "HORN", "HOST", "HOUR", "HUGE", "HUNT", "HURT", "ICON",
    "IDLE", "INCH", "INFO", "IRON", "ITEM", "JAIL", "JOIN", "JOKE", "JUMP", "JURY",
    "JUST", "KEEN", "KEEP", "KICK", "KILL", "KIND", "KING", "KISS", "KITE", "KNEE",
    "KNOT", "KNOW", "LACK", "LADY", "LAKE", "LAMB", "LAMP", "LAND", "LAST", "LATE",
    "LEAF", "LEAK", "LEAP", "LEFT", "LEND", "LENS", "LIFE", "LIFT", "LIKE", "LIME",
    "LINE", "LINK", "LIPS", "LIST", "LIVE", "LOAD", "LOAF", "LOAN", "LOCK", "LONG",
    "LOOK", "LOOP", "LORD", "LOSE", "LOSS", "LOST", "LOVE", "LUCK", "LUNG", "MADE",
    "MAID", "MAIL", "MAIN", "MAKE", "MALE", "MALL", "MANY", "MASK", "MASS", "MATE",
    "MAZE", "MEAL", "MEAN", "MEET", "MELT", "MENU", "MESS", "MILD", "MILE", "MILK",
    "MILL", "MIND", "MINE", "MINT", "MISS", "MIST", "MOOD", "MOON", "MORE", "MOST",
    "MOVE", "MUCH", "MUD", "NAME", "NAVY", "NEAR", "NECK", "NEED", "NEST", "NEWS",
    "NEXT", "NICE", "NINE", "NODE", "NONE", "NOSE", "NOTE", "OATH", "OBEY", "ODOR",
    "OILS", "OKAY", "ONCE", "ONLY", "ONTO", "OPEN", "ORAL", "OVER", "PACE", "PACK",
    "PAGE", "PAIN", "PAIR", "PALE", "PALM", "PARK", "PASS", "PAST", "PATH", "PEAK",
    "PEAR", "PEEL", "PEER", "PETS", "PICK", "PIER", "PILE", "PILL", "PINE", "PING",
    "PINK", "PINT", "PIPE", "PLAN", "PLAY", "PLEA", "PLOT", "PLUG", "POEM", "POET",
    "POLE", "POLL", "POND", "POOL", "POOR", "POPE", "PORK", "PORT", "POUR", "PRAY",
    "PULL", "PUMP", "PURE", "PUSH", "RACE", "RACK", "RAID", "RAIL", "RAIN", "RARE",
    "RATE", "READ", "REED", "REEL", "RELY", "RENT", "REST", "RICE", "RICH", "RIDE",
    "RING", "RISE", "RISK", "ROAD", "ROAR", "ROCK", "RODE", "ROLE", "ROLL", "ROOF",
    "ROOM", "ROOT", "ROPE", "RUIN", "RULE", "RUSH", "RUST", "SAFE", "SAIL", "SAKE",
    "SALE", "SALT", "SAND", "SAVE", "SCAN", "SEAL", "SEAM", "SEAT", "SEED", "SEEK",
    "SEEM", "SEEN", "SELF", "SELL", "SEND", "SHED", "SHIP", "SHOE", "SHOP", "SHOT",
    "SHOW", "SHUT", "SICK", "SIDE", "SIGH", "SIGN", "SILK", "SILO", "SING", "SINK",
    "SITE", "SIZE", "SKIN", "SKIP", "SLAP", "SLIP", "SLOT", "SLOW", "SNAP", "SNOW",
    "SOAP", "SOAR", "SOCK", "SOFA", "SOIL", "SOLO", "SOME", "SONG", "SOON", "SORE",
    "SOUL", "SOUP", "SOUR", "SPAN", "SPIN", "SPOT", "SPUR", "STAY", "STEM", "STEP",
    "STOP", "SUIT", "SURE", "SURF", "TAIL", "TAKE", "TALE", "TALK", "TALL", "TANK",
    "TAPE", "TASK", "TAXI", "TEAR", "TELL", "TERM", "TEST", "TEXT", "THAT", "THEM",
    "THEN", "THEY", "THIN", "THIS", "TIDE", "TIDY", "TIED", "TIER", "TILE", "TILL",
    "TINY", "TIRE", "TOAD", "TOLL", "TONE", "TOOK", "TOOL", "TOPS", "TORN", "TOSS",
    "TOUR", "TOWN", "TRAP", "TRAY", "TREE", "TRUE", "TUBE", "TUCK", "TUNE", "TURN",
    "TWIN", "TYPE", "UNIT", "UPON", "URGE", "USER", "VALE", "VARY", "VAST", "VEIL",
    "VEIN", "VENT", "VERB", "VERY", "VEST", "VETO", "VIEW", "VINE", "VOID", "VOLT",
    "VOTE", "WADE", "WAGE", "WAIT", "WAKE", "WALK", "WALL", "WANT", "WARD", "WARN",
    "WASH", "WAVE", "WEAK", "WEAR", "WEED", "WEEK", "WEEP", "WELL", "WENT", "WEST",
    "WHAT", "WHEN", "WHIP", "WIDE", "WIFE", "WILD", "WILL", "WIND", "WINE", "WING",
    "WIPE", "WIRE", "WISE", "WISH", "WITH", "WOLF", "WOOD", "WOOL", "WORD", "WORK",
    "WORM", "WRAP", "YARD", "YARN", "YEAR", "YELL", "YOGA", "ZERO", "ZONE", "ZOOM"
]

WORDS_5 = [
    "HEART", "EMBER", "ABUSE", "RESIN", "TREND", "PLANT", "LINEN", "ANIME", "NEMEA", "TREAT",
    "SCALE", "CORAL", "ARENA", "LANES", "ELAST", "TRADE", "RACER", "ACUTE", "DETOX", "ERECT",
    "ALERT", "ALTER", "AMBER", "ANGEL", "ANGER", "APPLE", "APRON", "ARISE", "ASIDE", "ASSET",
    "AVOID", "AWARD", "AWARE", "BADGE", "BAKER", "BASIC", "BASIS", "BEACH", "BEAST", "BEGIN",
    "BEING", "BELOW", "BENCH", "BIRTH", "BLACK", "BLADE", "BLANK", "BLAST", "BLEED", "BLEND",
    "BLESS", "BLIND", "BLOCK", "BLOOD", "BLOOM", "BOARD", "BOAST", "BOOST", "BRAIN", "BRAKE",
    "BRAND", "BRASS", "BRAVE", "BREAD", "BREAK", "BRICK", "BRIDE", "BRIEF", "BRING", "BROAD",
    "BROWN", "BRUSH", "BUILD", "CABIN", "CABLE", "CANAL", "CANDY", "CARGO", "CARRY", "CARVE",
    "CATCH", "CAUSE", "CHAIN", "CHAIR", "CHALK", "CHAMP", "CHANT", "CHARM", "CHART", "CHASE",
    "CHEAP", "CHECK", "CHEEK", "CHEER", "CHEST", "CHIEF", "CHILD", "CIVIL", "CLAIM", "CLAMP",
    "CLASS", "CLEAN", "CLEAR", "CLERK", "CLICK", "CLIFF", "CLIMB", "CLOCK", "CLOSE", "CLOTH",
    "CLOUD", "COACH", "COAST", "COUNT", "COURT", "COVER", "CRACK", "CRAFT", "CRANE", "CRASH",
    "CRAWL", "CRAZY", "CREAM", "CREEK", "CREST", "CRIME", "CRISP", "CROSS", "CROWD", "CROWN",
    "CRUSH", "CRUST", "DANCE", "DEATH", "DELAY", "DELTA", "DENSE", "DEPTH", "DRAFT", "DRAIN",
    "DRAMA", "DRANK", "DRAWN", "DREAM", "DRESS", "DRIFT", "DRILL", "DRINK", "DRIVE", "EAGER",
    "EARLY", "EARTH", "EIGHT", "ELITE", "EMPTY", "ENEMY", "ENJOY", "ENTER", "ENTRY", "EQUAL",
    "ERROR", "ESSAY", "EVENT", "EVERY", "EXACT", "EXIST", "EXTRA", "FAITH", "FALSE", "FANCY",
    "FAULT", "FAVOR", "FEAST", "FIBER", "FIELD", "FIFTH", "FIFTY", "FIGHT", "FINAL", "FIRST",
    "FLAME", "FLASH", "FLEET", "FLESH", "FLOAT", "FLOOD", "FLOOR", "FLOUR", "FLUID", "FOCUS",
    "FORCE", "FORTH", "FORTY", "FOUND", "FRAME", "FRESH", "FRONT", "FROST", "FRUIT", "GIANT",
    "GIVEN", "GLASS", "GLOBE", "GLORY", "GLOVE", "GRACE", "GRADE", "GRAIN", "GRAND", "GRANT",
    "GRAPE", "GRAPH", "GRASP", "GRASS", "GRAVE", "GREAT", "GREEN", "GREET", "GRIEF", "GRILL",
    "GROSS", "GROUP", "GROVE", "GUARD", "GUESS", "GUEST", "GUIDE", "HABIT", "HAPPY", "HARSH",
    "HEAVY", "HELLO", "HONEY", "HONOR", "HORSE", "HOTEL", "HOUSE", "HUMAN", "HUMOR", "IDEAL",
    "IMAGE", "INDEX", "INNER", "INPUT", "IRONY", "ISSUE", "JEWEL", "JOINT", "JUDGE", "JUICE",
    "KNIFE", "KNOCK", "KNOWN", "LABEL", "LABOR", "LARGE", "LASER", "LATER", "LAUGH", "LAYER",
    "LEARN", "LEAST", "LEAVE", "LEGAL", "LEMON", "LEVEL", "LEVER", "LIGHT", "LIMIT", "LINEN",
    "LIVER", "LOCAL", "LODGE", "LOGIC", "LOOSE", "LOVER", "LOWER", "LOYAL", "LUCKY", "LUNCH",
    "MAGIC", "MAJOR", "MAKER", "MANGO", "MARCH", "MATCH", "MAYOR", "MEDAL", "MEDIA", "MELON",
    "MERCY", "MERIT", "METAL", "METER", "MIGHT", "MINOR", "MODEL", "MONEY", "MONTH", "MORAL",
    "MOTOR", "MOUNT", "MOUSE", "MOUTH", "MOVIE", "MUSIC", "NAIVE", "NERVE", "NIGHT", "NOBLE",
    "NOISE", "NORTH", "NOVEL", "NURSE", "OCEAN", "OFFER", "OFTEN", "OLIVE", "ONION", "OPERA",
    "ORBIT", "ORDER", "ORGAN", "OTHER", "OUTER", "OWNER", "PAINT", "PANEL", "PANIC", "PAPER",
    "PARTY", "PASTA", "PATCH", "PAUSE", "PEACE", "PEACH", "PEARL", "PENNY", "PHASE", "PHONE",
    "PHOTO", "PIANO", "PIECE", "PILOT", "PINCH", "PIVOT", "PIZZA", "PLACE", "PLAIN", "PLANE",
    "PLAZA", "POINT", "POLAR", "POUND", "POWER", "PRESS", "PRICE", "PRIDE", "PRIME", "PRINT",
    "PRIOR", "PRIZE", "PROBE", "PROOF", "PROUD", "PROVE", "PULSE", "QUEEN", "QUERY", "QUEST",
    "QUICK", "QUIET", "RADAR", "RADIO", "RAISE", "RANCH", "RANGE", "RAPID", "RATIO", "REACH",
    "REACT", "READY", "REALM", "REFER", "RELAX", "REPLY", "RESET", "RIDER", "RIDGE", "RIGHT",
    "RIGID", "RIVAL", "RIVER", "ROBOT", "ROUND", "ROUTE", "ROYAL", "RULER", "RURAL", "SAINT",
    "SALAD", "SCENE", "SCENT", "SCOPE", "SCORE", "SCOUT", "SCRAP", "SEIZE", "SENSE", "SERVE",
    "SEVEN", "SHADE", "SHAFT", "SHAKE", "SHALL", "SHAME", "SHAPE", "SHARE", "SHARK", "SHARP",
    "SHEEP", "SHEET", "SHELF", "SHELL", "SHIFT", "SHINE", "SHIRT", "SHOCK", "SHOOT", "SHORE",
    "SHORT", "SHOUT", "SIGHT", "SKILL", "SKIRT", "SKULL", "SLATE", "SLEEP", "SLICE", "SLIDE",
    "SLOPE", "SMART", "SMELL", "SMILE", "SMOKE", "SNAKE", "SOLAR", "SOLID", "SOLVE", "SOUND",
    "SOUTH", "SPACE", "SPARE", "SPARK", "SPEAK", "SPEED", "SPELL", "SPEND", "SPICE", "SPILL",
    "SPINE", "SPLIT", "SPOKE", "SPOON", "SPORT", "STAFF", "STAGE", "STAIN", "STAIR", "STAKE",
    "STALE", "STAND", "STARE", "START", "STATE", "STEAM", "STEEL", "STEEP", "STEER", "STICK",
    "STILL", "STOCK", "STONE", "STORM", "STORY", "STRAP", "STRAW", "STRIP", "STUDY", "STUFF",
    "STYLE", "SUGAR", "SUITE", "SUPER", "SURGE", "SWAMP", "SWEAR", "SWEAT", "SWEEP", "SWEET",
    "SWIFT", "SWORD", "TABLE", "TASTE", "TEACH", "TEETH", "THANK", "THEME", "THERE", "THESE",
    "THICK", "THIEF", "THING", "THINK", "THIRD", "THOSE", "THREE", "THROW", "THUMB", "TIGER",
    "TIGHT", "TIMER", "TIRED", "TITLE", "TODAY", "TOOTH", "TOPIC", "TORCH", "TOTAL", "TOUCH",
    "TOUGH", "TOWEL", "TOWER", "TOXIC", "TRACE", "TRACK", "TRADE", "TRAIL", "TRAIN", "TRAIT",
    "TREAT", "TREND", "TRIAL", "TRICK", "TROOP", "TRUCK", "TRULY", "TRUNK", "TRUST", "TRUTH",
    "TULIP", "TWICE", "TWIST", "UNCLE", "UNDER", "UNION", "UNITE", "UNITY", "UNTIL", "UPPER",
    "UPSET", "URBAN", "USAGE", "USUAL", "VAGUE", "VALID", "VALUE", "VALVE", "VAPOR", "VAULT",
    "VENUE", "VERSE", "VIDEO", "VILLA", "VIRAL", "VIRUS", "VISIT", "VITAL", "VIVID", "VOCAL",
    "VOICE", "VOTER", "WAGON", "WASTE", "WATCH", "WATER", "WHEAT", "WHEEL", "WHERE", "WHICH",
    "WHILE", "WHITE", "WHOLE", "WIDOW", "WIDTH", "WOMAN", "WORLD", "WORRY", "WORSE", "WORST",
    "WORTH", "WOUND", "WRECK", "WRIST", "WRITE", "WRONG", "YACHT", "YEARN", "YIELD", "YOUNG",
    "YOUTH", "ZEBRA"
]

WORDS = WORDS_3 + WORDS_4 + WORDS_5


MAX_ITERATIONS = 200
MAX_RESTARTS = 50

def generate_grid(size=3):
    return [["_" for _ in range(size)] for _ in range(size)]



def find_slots(grid):
    slots = []
    rows = len(grid)
    cols = len(grid[0])

    
    for r in range(rows):
        cells = [
            (r, c)
            for c in range(cols)
            if grid[r][c] == "_"
        ]
        if len(cells) >= 2:
            slots.append({
                "id": f"A{r + 1}",
                "cells": cells
            })

   
    for c in range(cols):
        cells = [
            (r, c)
            for r in range(rows)
            if grid[r][c] == "_"
        ]
        if len(cells) >= 2:
            slots.append({
                "id": f"D{c + 1}",
                "cells": cells
            })

    return slots



def create_domains(slots):
    return {
        slot["id"]: [
            word
            for word in WORDS
            if len(word) == len(slot["cells"])
        ]
        for slot in slots
    }



def find_intersections(slots):
    intersections = {}

    for i in range(len(slots)):
        for j in range(i + 1, len(slots)):
            s1 = slots[i]
            s2 = slots[j]

            for p1, cell1 in enumerate(s1["cells"]):
                for p2, cell2 in enumerate(s2["cells"]):
                    if cell1 == cell2:
                        intersections[(s1["id"], s2["id"])] = (p1, p2)
                        intersections[(s2["id"], s1["id"])] = (p2, p1)

    return intersections



def conflicts(slot_id, word, assignment, intersections):
    count = 0

    
    for (s1, s2), (p1, p2) in intersections.items():
        if s1 == slot_id and s2 in assignment:
            if word[p1] != assignment[s2][p2]:
                count += 1

   
    for sid, other_word in assignment.items():
        if sid != slot_id and word == other_word:
            count += 1

    return count



def total_conflicts(assignment, intersections):
    count = 0
    checked = set()

   
    for (s1, s2), (p1, p2) in intersections.items():
        pair = tuple(sorted((s1, s2)))
        if pair in checked:
            continue
        checked.add(pair)
        if assignment[s1][p1] != assignment[s2][p2]:
            count += 1

    
    words = list(assignment.values())
    count += len(words) - len(set(words))

    return count



def random_assignment(slots, domains):
    assignment = {}
    used = set()

    shuffled = slots[:]
    random.shuffle(shuffled)

    for slot in shuffled:
        available = [
            word
            for word in domains[slot["id"]]
            if word not in used
        ]

        if not available:
            return None

        word = random.choice(available)
        assignment[slot["id"]] = word
        used.add(word)

    return assignment



def select_slot(slots, assignment, intersections):
    bad_slots = []

    for slot in slots:
        sid = slot["id"]
        if conflicts(sid, assignment[sid], assignment, intersections) > 0:
            bad_slots.append(sid)

    return random.choice(bad_slots) if bad_slots else None



def best_word(slot_id, domains, assignment, intersections):
    used = {
        word
        for sid, word in assignment.items()
        if sid != slot_id
    }

    best_score = float("inf")
    candidates = []

    for word in domains[slot_id]:
       
        if word in used:
            continue

        score = conflicts(
            slot_id,
            word,
            assignment,
            intersections
        )

        if score < best_score:
            best_score = score
            candidates = [word]
        elif score == best_score:
            candidates.append(word)

    return random.choice(candidates) if candidates else None



def solve(slots, domains, intersections, max_restarts=MAX_RESTARTS, max_iterations=MAX_ITERATIONS):
    history = []
    total_iter = 0

    for restart in range(1, max_restarts + 1):
        assignment = random_assignment(slots, domains)
        if assignment is None:
            continue

        initial_conf = total_conflicts(assignment, intersections)
        history.append({
            "restart": restart,
            "iteration": total_iter,
            "slot": "Initial Assignment",
            "word": "Random Init",
            "conflicts": initial_conf
        })

        for _ in range(max_iterations):
            total_iter += 1

            
            if total_conflicts(assignment, intersections) == 0:
                return assignment, restart, total_iter, history

            
            sid = select_slot(slots, assignment, intersections)
            if sid is None:
                break

            
            word = best_word(sid, domains, assignment, intersections)
            if word is None:
                break

            assignment[sid] = word
            post_conf = total_conflicts(assignment, intersections)

           
            history.append({
                "restart": restart,
                "iteration": total_iter,
                "slot": sid,
                "word": word,
                "conflicts": post_conf
            })

           
            if post_conf == 0:
                return assignment, restart, total_iter, history

    return None, None, total_iter, history



def build_grid(grid, slots, assignment):
    result = [row[:] for row in grid]
    for slot in slots:
        word = assignment[slot["id"]]
        for i, (r, c) in enumerate(slot["cells"]):
            result[r][c] = word[i]
    return result



def display(grid, slots, assignment, restarts, iterations, elapsed):
    print("\n" + "=" * 40)
    print("        SOLVED CROSSWORD")
    print("=" * 40)

    for row in grid:
        print("  " + " ".join(row))

    print("\nWord Placement")
    print("-" * 25)
    for slot in slots:
        slot_type = "Across" if slot["id"].startswith("A") else "Down"
        print(f"  {slot['id']} ({slot_type}) : {assignment[slot['id']]}")

    print("\nStatistics")
    print("-" * 25)
    print(f"  Grid Size    : {len(grid)}x{len(grid[0])}")
    print(f"  Slots        : {len(slots)}")
    print(f"  Restarts     : {restarts}")
    print(f"  Iterations   : {iterations}")
    print(f"  Time         : {elapsed:.6f} sec")
    print(f"  Unique Words : {len(set(assignment.values())) == len(assignment)}")
    print("\n[SUCCESS] Crossword solved successfully!")



def show_slots(slots, grid_size):
    print("\n" + "=" * 40)
    print("           SLOT VIEWER")
    print("=" * 40)
    print(f"Grid Size: {grid_size}x{grid_size} | Total Slots: {len(slots)}\n")

    across_slots = [s for s in slots if s["id"].startswith("A")]
    down_slots = [s for s in slots if s["id"].startswith("D")]

    print("Across Slots:")
    for slot in across_slots:
        row_num = slot["cells"][0][0] + 1
        print(f"  {slot['id']} -> Row {row_num} (Length: {len(slot['cells'])}, Cells: {slot['cells']})")

    print("\nDown Slots:")
    for slot in down_slots:
        col_num = slot["cells"][0][1] + 1
        print(f"  {slot['id']} -> Column {col_num} (Length: {len(slot['cells'])}, Cells: {slot['cells']})")



def show_intersections(intersections):
    print("\n" + "=" * 40)
    print("       INTERSECTION VIEWER")
    print("=" * 40)
    print(f"Total Intersections: {len(intersections) // 2}\n")

    seen = set()
    for (s1, s2), (p1, p2) in sorted(intersections.items()):
        pair = tuple(sorted((s1, s2)))
        if pair not in seen:
            seen.add(pair)
            print(f"  {s1} intersects {s2} at index ({p1}, {p2})")



def show_iteration_history(history):
    print("\n" + "=" * 40)
    print("        ITERATION HISTORY")
    print("=" * 40)

    if not history:
        print("No solving history available. Please solve a crossword first.")
        return

    print(f"Total Recorded Steps: {len(history)}\n")


    display_limit = 20
    if len(history) <= display_limit:
        steps_to_show = history
    else:
        steps_to_show = history[:10] + [{"ellipsis": True}] + history[-10:]

    step_counter = 1
    for item in steps_to_show:
        if "ellipsis" in item:
            print("  ... [ intermediate iterations omitted for brevity ] ...\n")
            continue

        print(f"Iteration {item['iteration']} (Restart {item['restart']}):")
        print(f"  Selected Slot = {item['slot']}")
        print(f"  Assigned Word = {item['word']}")
        print(f"  Conflicts     = {item['conflicts']}")
        print()
        step_counter += 1

    print("-" * 40)
    print("Conflict Reduction Tracking:")
    print("-" * 40)
    prev_conf = None
    for item in history:
        if item["conflicts"] != prev_conf:
            print(f"  Iteration {item['iteration']:3d} -> {item['conflicts']} conflicts")
            prev_conf = item["conflicts"]



def show_statistics(grid, slots, solution, restarts, iterations, elapsed):
    print("\n" + "=" * 40)
    print("         DETAILED STATISTICS")
    print("=" * 40)

    if solution is None:
        print("No solution data available. Please solve a crossword first.")
        return

    unique_count = len(set(solution.values()))
    total_slots = len(slots)
    grid_size = f"{len(grid)}x{len(grid[0])}"

    print(f"  Grid Size           : {grid_size}")
    print(f"  Number of Slots     : {total_slots}")
    print(f"  Dictionary Size     : {len(WORDS)} words ({len(WORDS_3)} 3-letter, {len(WORDS_4)} 4-letter, {len(WORDS_5)} 5-letter)")
    print(f"  Total Iterations    : {iterations}")
    print(f"  Total Restarts      : {restarts}")
    print(f"  Time Taken          : {elapsed:.6f} sec")
    print(f"  Unique Words Used   : {unique_count == total_slots} ({unique_count}/{total_slots} unique)")
    print(f"  Final Conflict Count: 0")
    print(f"  Success Status      : Solved Successfully")



def export_solution(filename, grid, slots, solution, restarts, iterations, elapsed, history):
    if solution is None:
        print("\n[!] No solved crossword to export. Please solve a crossword first.")
        return

    try:
        with open(filename, "w") as f:
            f.write("=" * 40 + "\n")
            f.write("      AI CROSSWORD SOLVER SOLUTION\n")
            f.write("  Min-Conflicts + Random Restart\n")
            f.write("=" * 40 + "\n\n")

            f.write("SOLVED GRID:\n")
            for row in grid:
                f.write("  " + " ".join(row) + "\n")
            f.write("\n")

            f.write("WORD PLACEMENTS:\n")
            f.write("-" * 25 + "\n")
            for slot in slots:
                slot_type = "Across" if slot["id"].startswith("A") else "Down"
                f.write(f"  {slot['id']} ({slot_type}) : {solution[slot['id']]}\n")
            f.write("\n")

            f.write("STATISTICS:\n")
            f.write("-" * 25 + "\n")
            f.write(f"  Grid Size           : {len(grid)}x{len(grid[0])}\n")
            f.write(f"  Number of Slots     : {len(slots)}\n")
            f.write(f"  Total Iterations    : {iterations}\n")
            f.write(f"  Total Restarts      : {restarts}\n")
            f.write(f"  Time Taken          : {elapsed:.6f} sec\n")
            f.write(f"  Unique Words Used   : {len(set(solution.values())) == len(solution)}\n")
            f.write(f"  Final Conflict Count: 0\n")
            f.write(f"  Success Status      : Solved Successfully\n\n")

            f.write("CONFLICT REDUCTION SUMMARY:\n")
            f.write("-" * 25 + "\n")
            prev_conf = None
            for item in history:
                if item["conflicts"] != prev_conf:
                    f.write(f"  Iteration {item['iteration']:3d} -> {item['conflicts']} conflicts\n")
                    prev_conf = item["conflicts"]

        print(f"\n[+] Solution exported successfully to '{filename}'")
    except Exception as e:
        print(f"\n[!] Error exporting solution: {e}")


def main():
    grid_size = 3
    grid = generate_grid(grid_size)
    slots = find_slots(grid)
    domains = create_domains(slots)
    intersections = find_intersections(slots)

    solution = None
    restarts = None
    iterations = 0
    elapsed = 0.0
    history = []
    final_grid = grid

    while True:
        print("\n" + "=" * 34)
        print("       AI CROSSWORD SOLVER")
        print("  Min-Conflicts + Random Restart")
        print("=" * 34)
        print(f"Current Grid: {grid_size}x{grid_size}")
        print("1. Solve Crossword")
        print("2. Show Slots")
        print("3. Show Intersections")
        print("4. Show Iteration History")
        print("5. Show Statistics")
        print("6. Export Solution")
        print("7. Exit")
        print("=" * 34)

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            print("\nSelect Grid Size:")
            print("  1. 3x3 Grid")
            print("  2. 4x4 Grid")
            print("  3. 5x5 Grid")
            print(f"  4. Keep current ({grid_size}x{grid_size})")
            size_choice = input("Enter choice (1-4, default 4): ").strip()

            if size_choice == "1":
                grid_size = 3
            elif size_choice == "2":
                grid_size = 4
            elif size_choice == "3":
                grid_size = 5

           
            grid = generate_grid(grid_size)
            slots = find_slots(grid)
            domains = create_domains(slots)
            intersections = find_intersections(slots)

           
            valid = True
            for slot in slots:
                if not domains[slot["id"]]:
                    print(f"\n[!] No word available in dictionary for slot {slot['id']}")
                    valid = False
                    break

            if not valid:
                continue

            print(f"\nSolving {grid_size}x{grid_size} Crossword with Min-Conflicts + Random Restart...")
            start_time = time.time()

            solution, restarts, iterations, history = solve(
                slots,
                domains,
                intersections
            )
            elapsed = time.time() - start_time

            if solution:
                final_grid = build_grid(grid, slots, solution)
                display(final_grid, slots, solution, restarts, iterations, elapsed)
            else:
                print("\n[FAILED] No solution found within the restart and iteration limit.")

        elif choice == "2":
            show_slots(slots, grid_size)

        elif choice == "3":
            show_intersections(intersections)

        elif choice == "4":
            show_iteration_history(history)

        elif choice == "5":
            show_statistics(final_grid, slots, solution, restarts, iterations, elapsed)

        elif choice == "6":
            default_file = "crossword_solution.txt"
            filename_input = input(f"Enter filename (default: {default_file}): ").strip()
            filename = filename_input if filename_input else default_file
            export_solution(filename, final_grid, slots, solution, restarts, iterations, elapsed, history)

        elif choice == "7":
            print("\nThank you for using AI Crossword Solver. Goodbye!\n")
            break

        else:
            print("\n[!] Invalid choice. Please enter a number between 1 and 7.")



if __name__ == "__main__":
    main()
