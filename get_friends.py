import tweepy
import pickle

ALL_PEOPLE = {
    'test_s': ['Cryptoyieldinfo', 'stakeandstack', 'FTMAlerts', 'YieldMonitor', 'BBO_gmon3y',
               'ThinkingLSD', 'KariyaKanav', 'ngustafson21', 'amytongwu'],
    'test_d': ['mrjasonchoi', 'PastryETH', 'santiagoroel', 'gabagooldoteth', 'darrenlautf',
               '3azima85'],
    'coinfund': ['jbrukh', 'leidina_', 'AustinBarack', 'EvanTheFeng', 'coin_christian_', 'sethginns', 'PallaviGondi',
                 'JonCampagna', 'VanessaGrellet_', 'coinfund_io', 'flexthought'],

    'echanism': ['wvaeu', 'WarcMeinstein', 'benjaminsimon97', 'Daryllautk', 'Rewkang'],

    'dragonfly': ['dragonfly_cap', 'hosseeb', 'LindsayxLin', 'ashwinrz', 'miagegedeng', 'celiawan2', 'tomhschmidt',
                  'alpackaP', 'k_zerrudo', 'nanspr0', 'lzdiao', 'jonitzler', 'sanlsrni'],

    'multicoin': ['TusharJain_', 'KyleSamani', 'Mable_Jiang', 'HC_Xie__', 'shayonsengupta', 'mattshap1',
                  'johnrobertreed', 'VinnyLingham'],

    'paradigm': ['arjunblj', 'caseykcaruso', 'jimprosser', '_Dave__White_', 'samczsun', 'FEhrsam', '_charlienoyes',
                 'matthuang', 'hasufl', '_anishagnihotri', 'danrobinson', 'TylerCrimm', 'alanapalmedo',
                 'jordan_l_qualls', 'kevinxpang', 'g_co', 'paradigm'],

    'ac': ['zhusu', 'kyled116', 'YamaZhang'],

    'delphi': ['Delphi_Digital', 'YanLiberman', 'mediodelphi', 'Paul_Burlage', 'anildelphi', 'ZeMariaMacedo',
               'gillinghammer', 'ashwathbk', 'Shaughnessy119', 'Jeremystormsky', 'jeremyongws', 'jiminstupid',
               'FloodCapital', 'larry0x', 'lex_node', 'rsarrow', 'Kevin_Kelly_II', 'pierskicks', 'genye0h',
               'JonathanErlichL', 'Bitcoin_Sage', 'thejewforu', 'delphiintern', 'notatugboat', 'rrridges', 'Alex_Ged',
               'wtpiner', 'DrewAHenderson', 'WynnLemmons', 'CoalieBee', 'sarfang_', 'Crypt0___F1sh', 'theprivileges',
               'NotSoAnonJoo', 'OpulentCoffee'],

    'framework': ['hiFramework', 'RoyLearner', 'FRAMEWORKintern', '_dwasse', 'b_potts23', '0x_Osprey', 'im_manderson',
                  'pythianism'],

    'placeholder': ['placeholdervc', 'alexhevans', 'cburniske', 'mlphresearch', 'BradUSV', 'jmonegro'],

    'egirl': ['egirl_capital', 'CL207', 'scupytrooples', 'DegenSpartan', 'mewn21', 'loomdart', 'evabeylin',
              'AutomataEmily', 'bigmagicdao', 'hedgedhog7', 'pet3rpan_', 'knlae_', 'five5brown_eyes',
              'CryptoCatVC', 'miyuki_crypto', 'Fjvdb7', 'jeff_w1098'],

    'defiance': ['DeFianceCapital', 'Arthur_0x', 'thegreenbutton_', '0xWangarian', 'bottomd0g', 'jteam0x',
                 'stateroot'],

    'parafi': ['paraficapital', 'santiagoroel', 'mhonkasalo', 'n2ckchong', 'kyedidbotton', 'AdrianUberto', 'adamcader_',
               'yazshama', 'CorinnaRao', 'anjan_vinod'],

    'cms_holdings': ['cmsholdings', 'backbooked', 'cmsintern', 'cmsbagholdings', 'robertjcho', '__Swurve__',
                     'mackrypt0', 'cewh1te', 'zercb9', 'RDuthe'],

    'polychain': ['polychaincap', 'throughnothing', 'polychainlabs', 'eKRENZKE', 'JacobPPhillips', 'TekinSalimi',
                  'BenPerszyk', 'realSherwinD', 'rwitoff', 'sjrosenblum', 'aharshner', 'niraj', 'ssbrooks5', 'zxocw'],

    'spartan': ['TheSpartanGroup', 'mrjasonchoi', 'melmelmelting', 'Chetanya_K', 'Bart_Mahendran', 'gabrieltanhl',
                'kapursanat', 'CasperJohansen', 'itzjustcal', 'SpartanBlack_1'],

    'pantera': ['PanteraCapital', 'joeykrug', 'veradittakit', 'tinathesis', 'dan_pantera', 'lstephanian', 'FranklinBi',
                'tradergirlsuki', 'Erik_M_Lowe', 'emmarosepb', 'RonGlantz', 'CatsFoley', 'tradergirlsuki'],

    'sino_global': ['SinoGlobalCap', 'mattysino', 'dermotmcg', 'OmniscientAsian', 'sallywang666', 'TTx0x', 'cweihan',
                    'Aluirl'],

    'zee_prime': ['Fiskantes', 'mattigags', 'BrhelMichal', 'GregusJakub', 'ZeePrimeCap'],

    'jump': ['jumpcapital', 'zsparta', 'TheChicagoVC', 'KariyaKanav'],

    'lightspeed': ['lightspeedvp', 'amytongwu', 'mercebent', 'lolitataub', 'semil', 'adamwgoldberg', 'jeremysliew'],

    'divergence': ['divdotvc', 'cjliu49', 'gpl_94', '_bridgeharris'],

    'hashed': ['hashed_official', 'iamjosephyoung', 'baekkyoumkim', 'Hashed_HongPro', 'ethankim77', 'ryankim0x',
               'yk_rha', 'off_jinwoo', 'seojoonkim', 'timmy_sangwoo'],

    'blockchain': ['blockchaincap', '_kinjalbshah', 'pbartstephens', '_alekslarsen', 'CremeDeLaCrypto',
                   'h_joshua_rivera', 'wbrads'],

    'a16z': ['a16z', 'cdixon', 'AriannaSimpson', 'katie_haun', 'sriramk', 'milesjennings', 'alive_eth', 'CryptoClayman',
             '0xMasonH', '_jamico', 'dhaber', 'sumeet724', 'ChrisLyons', 'VirtualElena', 'WuCarra', 'eddylazzarin',
             'janehk', 'Tocelot'],

    'usv': ['usv', 'dgabeau', 'nickgrossman', 'fredwilson'],

    'lemniscap': ['Lemniscap', 'stonecoldpat0', 'Roder1k', 'shaishavhk', 'Realsantos1905', 'grisacerne',
                  'sjors_lemniscap'],

    'kx': ['1kxnetwork', 'HeyoChristopher', 'dberenzon', 'lalleclausen', 'nichanank', 'pet3rpan_'],

    'confirmation': ['1confirmation', 'NTmoney', 'richardchen39'],

    'maven11': ['Maven11Capital', 'Balder1010', 'PS__M11', 'Michiel_AirPlus', 'VVojtek_P', 'darius_rye', 'JCvdPlas',
                'jochemwieringa'],

    'defialliance': ['defialliance', 'rriccio', 'DangerWillRobin', 'panekkkk', 'adampatel23', 'lmrankhan', 'DeFi_0x',
                     'QwQiao', 'andreasantichio', 'jocelynrobancho', 'shutterbugsid', 'kichsr', 'joel_john95',
                     'jasondchap'],

    'semantic': ['SemanticVC', 'stefanobernardi', 'yanroux', 'sh3lko'],

    'fabric': ['fabric_vc', 'richardmuirhead', 'sniedercorn', 'ahansjee', 'deseventral', 'LataPersson', 'nosremenai',
               'JulienThevenard', 'AlainFalys', 'tee_ganbold', 'anastasiya_vc', 'MerschMax_'],

    'dekrypt': ['DekryptCapital', 'jonathantallen1'],

    'greenfield_one': ['Greenfield1One', 'LeBastif', 'JaschaSamadi', 'felix_macht', 'heygleb', '0xElle'],

    'thelao': ['TheLAOOfficial', 'awrigh01', 'ameensol', 'pridesai', 'Ng888888Ng', 'pdesai587', 'fabianffebo',
               'gurkin_sergey', 'David_Kji', 'YuanXue2011', 'UBIpromoter'],

    'robot': ['robotventures', 'rleshner', 'tarunchitra'],

    'fisher8cap': ['fisher8cap', '0xkinnif', '0x_kertapati', '2x1q7f9'],

    'slow': ['slow', 'jillrgunter', 'crabbylions', 'KevinColleran', 'lessin'],

    'iosg': ['IOSGVC', 'Ishanee0x', 'xinshudong', 'RayXiao11', 'ergokhaner', 'JinzhouLin', 'DenizOmer', 'IosgJas',
             'momir_amidzic'],

    'ngc': ['NGC_Ventures', 'keyahayek', 'Andrea__Chang', 'tony_gu'],

    'ideo': ['IDEOVC', 'ianIDEO', 'parisrouz', 'taratan', 'bramanathan', 'GavinMcDermott', 'Joe_Gerber_', 'delitzer'],

    'electric': ['ElectricCapital', 'avichal', 'puntium', 'MariaShen', 'thuanlee', 'jubos'],

    'scalar': ['scalarcapital', 'jcliff42', 'ljxie', 'cyounessi1', 'KerryWo101', 'jordanwpalmer'],

    'sfermion': ['Sfermion_', 'AndrewSteinwold', 'Dan_Patterson_', 'iamjohnegan'],

    'lattice': ['lattice_capital', 'reganbozman', 'MikeZajko'],

    'sv': ['Official4SV', 'Ubirajaru', 'luiscfmcrypto'],

    'rcapital': ['4RCapital', 'DeFi_Dad', 'emiliomaglione', 'ej__rogers', 'keegan_selby', 'rahilla'],

    'd64': ['D64vc', 'aaronmcdnz', '_quinnab', 'LordTylerWard'],

    'variant': ['variantfund', 'StaniKulechov', 'spencernoon', 'Cooopahtroopa', 'jessewldn', 'jonitzler'],

    'hypershpere': ['hypersphere_', 'jackbplatts', 'amelia_cai_', 'JTMcGrath', 'amirroral'],

    'boostvc': ['BoostVC', 'BraytonKey', 'MaddieCallander', 'MaddieCallander'],

    'bitscale': ['BitscaleCapital', 'kazhiloti', 'stefanoschiavi'],

    'p2p': ['P2Pvalidator', '_vshapovalov', 'Lomashuk', 'aleko_an', 'abondar92', 'katyaandme'],

    'amentum': ['Amentum', 'Steven_McKie', 'theesehands'],

    'tomahawkvc': ['tomahawk_vc', 'connorbmilner', 'cediwaldburger', 'claudedonze'],

    'decimal': ['8Decimal', 'remi_gai', 'yubo_ruan'],

    'gbv': ['gbvofficial', 'LeslieisHODLing', '0xminion', 'sungjae_han', '0xbabble', '0xArchie'],

    'blocktower': ['BlockTower', 'AriDavidPaul', 'AviFelman', 'matthewgoetz', 'xxstevelee', 'coreyj_miller',
                   'MikeBucella',
                   'rahul_rai121', 'SanatVC', 'brichardson__'],

    'alphaseekers': ['paulcr2009', 'sereja_chan', 'iamDCinvestor', '0xtuba', 'DeFiGod1', 'scupytrooples',
                     'MapleLeafCap',
                     'sassal0x', 'bantg', 'hasufl']
}

twitter_open_key = 'JzmIdfXOWGnSNfPKGryj8KHkQ'
twitter_secret_key = '1uvwjxOSnYgJwIik6oCL4nclzVIRgPzgaR4jgkbGuUfOOGwOT6'

twitter_token_open = '1380934730657505281-VquvHeQiG9VdXr3zzuF9nvQalmlgCf'
twitter_token_secret = 'jgCjdNrzmHJoQnafJnBi1PGGBwSmC47nC7clnhNbUuY94'


def get_friends(people: list, api_twitter):
    dict_friends = {}
    for person in people:
        friends = []
        print(person)
        try:
            for friend in tweepy.Cursor(api_twitter.friends_ids, person).items():
                friends.append(friend)
            dict_friends[person] = friends
        except:
            print(f'Error for {person}')
    return dict_friends


def save_obj(obj, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(twitter_open_key, twitter_secret_key)
    auth.set_access_token(twitter_token_open, twitter_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
    ans = {}
    for k, v in ALL_PEOPLE.items():
        dict_friends = get_friends(v, api)
        ans[k] = dict_friends
    save_obj(ans, 'friends')
