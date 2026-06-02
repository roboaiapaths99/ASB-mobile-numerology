import re
from datetime import datetime
from collections import Counter

class NumerologyConsultation:
    
    def __init__(self, name, dob, mobile_number, challenges):
        self.name = name
        self.dob = dob
        self.mobile_number = mobile_number
        self.challenges = challenges
        self.consultation_date = datetime.now().strftime("%d/%m/%Y")
    
    def clean_mobile(self):
        """Return only digits from mobile number"""
        return re.sub(r"\D", "", self.mobile_number)
    
        
    def calculate_moolank(self):
        """Calculate Moolank (birth day reduced to single digit)"""
        day = int(self.dob.split('/')[0])
        while day > 9:
            day = sum(int(d) for d in str(day))
        return day
    
    def calculate_bhagyank(self):
        """Calculate Bhagyank (sum of full date of birth)"""
        date_str = self.dob.replace('/', '')
        total = sum(int(d) for d in date_str)
        while total > 9:
            total = sum(int(d) for d in str(total))
        return total
    
    def generate_name_dob_grid(self):
        """Generate Lo Shu Grid based on DOB only"""
        
        # dob digits (ignore 0)
        dob_digits = [d for d in self.dob if d.isdigit() and d != "0"]

        count = Counter(dob_digits)

        grid_structure = [
            [4,9,2],
            [3,5,7],
            [8,1,6]
        ]

        grid = []

        for row in grid_structure:
            r = []
            for num in row:
                c = count.get(str(num),0)

                if c == 0:
                    r.append("-")
                else:
                    r.append(str(num)*c)

            grid.append(r)

        return grid
    
    def generate_numeroscope_grid(self):
        """Generate Lo Shu Numeroscope Grid"""
        mobile = self.clean_mobile()
        
        # ignore zero in numeroscope
        digits = [d for d in mobile if d != "0"]
        count = Counter(digits)

        # Lo Shu Grid Structure
        grid = [
            [4, 9, 2],
            [3, 5, 7],
            [8, 1, 6]
        ]

        result = []

        for row in grid:
            r = []
            for num in row:
                c = count.get(str(num), 0)
                if c == 0:
                    r.append("-")
                else:
                    r.append(str(num) * c)
            result.append(r)

        return result
    
    def calculate_mobile_total(self):
        """Calculate mobile number total"""
        mobile = self.clean_mobile()
        
        total = sum(int(d) for d in mobile)
        while total > 9:
            total = sum(int(d) for d in str(total))
        return total
    
    def classify_numbers(self):
        """Classify numbers as Friendly/Enemy/Neutral based on compatibility table"""
        moolank = self.calculate_moolank()
        bhagyank = self.calculate_bhagyank()
        
        # Compatibility table
        compatibility = {
            1: {"friendly": [1,2,3,5,9], "enemy": [8], "neutral": [4,6,7]},
            2: {"friendly": [1,3,5], "enemy": [4,8,9], "neutral": [2,6,7]},
            3: {"friendly": [1,2,3,5], "enemy": [6], "neutral": [4,7,8,9]},
            4: {"friendly": [1,6,7], "enemy": [2,4,8,9], "neutral": [3,5]},
            5: {"friendly": [1,2,3,5,6], "enemy": [], "neutral": [4,7,8,9]},
            6: {"friendly": [4,5,6,7], "enemy": [3], "neutral": [1,2,8,9]},
            7: {"friendly": [1,4,5,6], "enemy": [], "neutral": [2,3,7,8,9]},
            8: {"friendly": [3,5,6], "enemy": [1,2,4,8], "neutral": [7,9]},
            9: {"friendly": [1,3,5], "enemy": [2,4], "neutral": [6,7,8,9]}
        }
        
        moolank_comp = compatibility.get(moolank, {"friendly": [1,2,3,5,9], "enemy": [8], "neutral": [4,6,7]})

        # Use only Moolank classification (date sum)
        friendly = set(moolank_comp['friendly'])
        enemy = set(moolank_comp['enemy'])
        neutral = set(moolank_comp['neutral'])
        
                
        # Special rule: If Moolank or Bhagyank is 3, add 6 to enemy (and vice versa)
        if moolank == 3 or bhagyank == 3:
            enemy.add(6)
            neutral.discard(6)
        if moolank == 6 or bhagyank == 6:
            enemy.add(3)
            neutral.discard(3)
        
        return {
            "friendly": sorted(friendly),
            "enemy": sorted(enemy),
            "neutral": sorted(neutral)
        }
    
    def analyze_pairs(self):
        """Analyze pairs of digits in mobile number with correct pair generation"""
        pairs = []
        pair_analysis = []
        
        # Generate consecutive pairs correctly
        mobile = self.clean_mobile()
        for i in range(len(mobile) - 1):
            pair = mobile[i:i+2]
            pairs.append(pair)
        
        # Good Numbers (bring positive results)
        good_pairs = {
            '12': 'Savings', '21': 'Savings',
            '15': 'Exam success, power', '51': 'Exam success, power',
            '17': 'Leadership, government contracts', '71': 'Leadership, government contracts',
            '19': 'Unexpected money, stock market', '91': 'Unexpected money, stock market',
            '25': 'Oratory power, occult knowledge', '52': 'Oratory power, occult knowledge',
            '29': 'Self earned money', '92': 'Self earned money',
            '36': 'Multi-talented, religious', '63': 'Multi-talented, religious',
            '37': 'Top position, long success', '73': 'Top position, long success',
            '38': 'Sales and property business', '83': 'Sales and property business',
            '39': 'Good debator', '93': 'Good debator',
            '57': 'Business success, public speaker', '75': 'Business success, public speaker',
            '59': 'Sharp mind, technical knowledge', '95': 'Sharp mind, technical knowledge',
            '69': 'Creativity, fashion, events', '96': 'Creativity, fashion, events'
        }
        
        # Bad Numbers (create problems)
        bad_pairs = {
            '13': 'Financial loss, accident', '31': 'Financial loss, accident',
            '14': 'Secret enemies', '41': 'Secret enemies',
            '16': 'Job loss, health issues', '61': 'Job loss, health issues',
            '18': 'Family issues', '81': 'Family issues',
            '23': 'Children embarrassment', '32': 'Children embarrassment',
            '24': 'Mood swings', '42': 'Mood swings',
            '26': 'Education hurdles', '62': 'Education hurdles',
            '27': 'Joint pain, profession problems', '72': 'Joint pain, profession problems',
            '28': 'Depression, addiction', '82': 'Depression, addiction',
            '34': 'Breathing issues', '43': 'Breathing issues',
            '35': 'Financial losses', '53': 'Financial losses',
            '45': 'Court/hospital issues', '54': 'Court/hospital issues',
            '46': 'Skin disease', '64': 'Skin disease',
            '48': 'Stress, depression', '84': 'Stress, depression',
            '58': 'Financial loss', '85': 'Financial loss',
            '78': 'Loneliness', '87': 'Loneliness',
            '79': 'Career ups and downs', '97': 'Career ups and downs',
            '89': 'Aggression', '98': 'Aggression',
            '47': 'Clever personality', '74': 'Clever personality',
            '49': 'Success after hard work', '94': 'Success after hard work',
            '56': 'Shy nature', '65': 'Shy nature',
            '67': 'Music lover', '76': 'Music lover',
            '68': 'Good for doctors', '86': 'Good for doctors'
        }
        
        # Classify each pair
        for i, pair in enumerate(pairs, 1):  # Start serial number from 1
            if pair in good_pairs:
                pair_analysis.append({
                    'serial': i,  # Start from 1
                    'pair': pair, 
                    'type': 'Good', 
                    'meaning': good_pairs[pair]
                })
            elif pair in bad_pairs:
                pair_analysis.append({
                    'serial': i,  # Start from 1
                    'pair': pair, 
                    'type': 'Bad', 
                    'meaning': bad_pairs[pair]
                })
            else:
                # Default classification for pairs not in lists - changed to Bad
                pair_analysis.append({
                    'serial': i,  # Start from 1
                    'pair': pair, 
                    'type': 'Bad',  # Changed from 'Neutral' to 'Bad'
                    'meaning': 'Challenging combination'
                })
        
        return pair_analysis
    
    def get_recommended_totals(self):
        """Get recommended mobile number totals without duplicates"""
        moolank = self.calculate_moolank()
        bhagyank = self.calculate_bhagyank()
        
        # Compatibility table
        compatibility = {
            1: {"friendly": [1,2,3,5,9], "enemy": [8], "neutral": [4,6,7]},
            2: {"friendly": [1,3,5], "enemy": [4,8,9], "neutral": [2,6,7]},
            3: {"friendly": [1,2,3,5], "enemy": [6], "neutral": [4,7,8,9]},
            4: {"friendly": [1,6,7], "enemy": [2,4,8,9], "neutral": [3,5]},
            5: {"friendly": [1,2,3,5,6], "enemy": [], "neutral": [4,7,8,9]},
            6: {"friendly": [4,5,6,7], "enemy": [3], "neutral": [1,2,8,9]},
            7: {"friendly": [1,4,5,6], "enemy": [], "neutral": [2,3,7,8,9]},
            8: {"friendly": [3,5,6], "enemy": [1,2,4,8], "neutral": [7,9]},
            9: {"friendly": [1,3,5], "enemy": [2,4], "neutral": [6,7,8,9]}
        }
        
        moolank_friendly = compatibility.get(moolank, {"friendly": [1,2,3,5,9]})['friendly']
        bhagyank_friendly = compatibility.get(bhagyank, {"friendly": [1,2,3,5,9]})['friendly']
        
        # Combine and remove duplicates, then sort
        recommended = set(moolank_friendly + bhagyank_friendly)
        return sorted(recommended)
    
    def generate_remedies(self):
        """Generate numerology remedies with color and crystal recommendations"""
        moolank = self.calculate_moolank()
        
        # Lucky directions based on Moolank
        directions = {
            1: ['East', 'North'],
            2: ['South', 'East'],
            3: ['North', 'East'],
            4: ['South', 'West'],
            5: ['North', 'South'],
            6: ['South', 'East'],
            7: ['North', 'West'],
            8: ['South', 'West'],
            9: ['North', 'East']
        }
        
        # Color recommendations based on Primary Numerology Number
        color_recommendations = {
            1: {'planet': 'Sun', 'color': 'Red', 'avoid': ['Black']},
            2: {'planet': 'Moon', 'color': 'White', 'avoid': ['Black']},
            3: {'planet': 'Jupiter', 'color': 'Yellow', 'avoid': ['White']},
            4: {'planet': 'Rahu', 'color': 'Black/Grey', 'avoid': []},
            5: {'planet': 'Mercury', 'color': 'Green', 'avoid': []},
            6: {'planet': 'Venus', 'color': 'White', 'avoid': ['Yellow']},
            7: {'planet': 'Ketu', 'color': 'Black/Grey', 'avoid': []},
            8: {'planet': 'Saturn', 'color': 'Black', 'avoid': []},
            9: {'planet': 'Mars', 'color': 'Red', 'avoid': []}
        }
        
        # Crystal remedies for missing numbers
        crystal_remedies = {
            1: 'Sunstone',
            2: 'Moonstone',
            3: 'Citrine',
            4: 'Tiger Eye',
            5: 'Green Aventurine',
            6: 'Pyrite',
            7: 'Smoky Quartz',
            8: 'Amethyst',
            9: 'Red Jasper'
        }
        
        # Find missing numbers and recommend crystals
        missing_numbers = self.get_missing_numbers_from_grid()
        recommended_crystals = [crystal_remedies[num] for num in missing_numbers]
        
        # Get color info
        color_info = color_recommendations.get(moolank, {
            'planet': 'Unknown',
            'color': 'Mixed',
            'avoid': []
        })
        
        return {
            'directions': directions.get(moolank, ['East', 'North']),
            'color_info': color_info,
            'crystals': recommended_crystals
        }
    
    def calculate_energy_score(self):
        """Calculate energy score (0-100) based on numeroscope grid"""
        grid = self.generate_numeroscope_grid()
        score = 0
        
        # Count digits from grid
        for row in grid:
            for cell in row:
                if cell == "-":
                    score += 5  # Missing numbers
                elif len(cell) == 1:
                    score += 10  # Single occurrence
                else:
                    score += 8  # Multiple occurrences
        
        return score
    
    def get_missing_numbers(self):
        """Find missing numbers from 1-9 not present in mobile number"""
        mobile = self.clean_mobile()
        
        digits = set(d for d in mobile if d != "0")
        missing = []
        
        for i in range(1, 10):
            if str(i) not in digits:
                missing.append(i)
        
        return missing
    
    def get_missing_numbers_from_grid(self):
        """Find missing numbers from 1-9 not present in Lo Shu Grid"""
        grid = self.generate_name_dob_grid()
        present_numbers = set()
        
        for row in grid:
            for cell in row:
                if cell != "-" and cell != "":
                    # Extract the number from the cell (could be "2", "22", etc.)
                    for num in cell:
                        if num.isdigit():
                            present_numbers.add(int(num))
        
        missing = []
        for i in range(1, 10):
            if i not in present_numbers:
                missing.append(i)
        
        return missing
    
    def get_number_compatibility(self):
        """Get number compatibility system"""
        moolank = self.calculate_moolank()
        
        # Number compatibility table
        compatibility = {
            1: {'friendly': [1,2,3,5,9], 'enemy': [8], 'neutral': [4,6,7]},
            2: {'friendly': [1,3,5], 'enemy': [4,8,9], 'neutral': [2,6,7]},
            3: {'friendly': [1,2,3,5], 'enemy': [6], 'neutral': [4,7,8,9]},
            4: {'friendly': [1,6,7], 'enemy': [2,4,8,9], 'neutral': [3,5]},
            5: {'friendly': [1,2,3,5,6], 'enemy': [], 'neutral': [4,7,8,9]},
            6: {'friendly': [4,5,6,7], 'enemy': [3], 'neutral': [1,2,8,9]},
            7: {'friendly': [1,4,5,6], 'enemy': [], 'neutral': [2,3,7,8,9]},
            8: {'friendly': [3,5,6], 'enemy': [1,2,4,8], 'neutral': [7,9]},
            9: {'friendly': [1,3,5], 'enemy': [2,4], 'neutral': [6,7,8,9]}
        }
        
        mobile_total = self.calculate_mobile_total()
        user_compatibility = compatibility.get(moolank, {
            'friendly': [1,2,3,5,9], 
            'enemy': [8], 
            'neutral': [4,6,7]
        })
        
        # Check compatibility with mobile total
        if mobile_total in user_compatibility['friendly']:
            compatibility_status = 'Compatible ✅'
        elif mobile_total in user_compatibility['enemy']:
            compatibility_status = 'Incompatible ❌'
        else:
            compatibility_status = 'Neutral ⚖️'
        
        return {
            'user_number': moolank,
            'mobile_total': mobile_total,
            'compatibility_table': user_compatibility,
            'compatibility_status': compatibility_status
        }
    
    def generate_consultation_report(self):
        """Generate complete consultation report with final logic"""
        pair_analysis = self.analyze_pairs()
        bad_count = sum(1 for p in pair_analysis if p['type'] == 'Bad')
        good_count = sum(1 for p in pair_analysis if p['type'] == 'Good')
        
        # Final report logic (no neutral pairs anymore)
        if good_count > bad_count:
            final_result = "Positive Mobile Number ✅"
            interpretation = f"Your mobile number has majority Good pairs which is favorable. It may provide:\n\n• Career growth\n• Good health\n• Positive mindset\n• Harmonious family life\n• Financial stability"
        elif bad_count > good_count:
            final_result = "Negative Mobile Number ❌"
            interpretation = f"Change of mobile number is recommended as the mobile number comprises majority of Bad pairs which may cause:\n\n• Career issues\n• Health issues\n• Aggression\n• Negative thoughts\n• Family life problems\n\nHowever it may also provide:\n\n• Good self attitude\n• Administration qualities\n• Money savings"
        else:
            final_result = "Balanced Mobile Number ⚖️"
            interpretation = f"Your mobile number has equal Good and Bad pairs. This creates a mixed energy that may provide both opportunities and challenges. Regular numerology remedies are recommended."
        
        return {
            'client_info': {
                'name': self.name,
                'consultation_date': self.consultation_date,
                'dob': self.dob,
                'mobile': self.mobile_number,
                'challenges': self.challenges
            },
            'moolank': self.calculate_moolank(),
            'bhagyank': self.calculate_bhagyank(),
            'mobile_total': self.calculate_mobile_total(),
            'name_dob_grid': self.generate_name_dob_grid(),
            'mobile_grid': self.generate_numeroscope_grid(),
            'energy_score': self.calculate_energy_score(),
            'classification': self.classify_numbers(),
            'missing_numbers': self.get_missing_numbers(),
            'recommended_totals': self.get_recommended_totals(),
            'pair_analysis': pair_analysis,
            'pair_summary': {
                'good': good_count,
                'bad': bad_count
            },
            'compatibility': self.get_number_compatibility(),
            'final_result': final_result,
            'interpretation': interpretation,
            'remedies': self.generate_remedies()
        }
