import pandas as pd
import numpy as np
import os
import csv
import json

from fuzzywuzzy import fuzz
from enum import IntFlag, IntEnum
import unicodedata, unittest
import importlib.resources as pkg_resources
from difflib import ndiff

list_elf = ['vof', 'bv', 'nv', 'avv', 'groupe', 'vba', 'operative', 'limited', 'cooperative', 'coop', 'co', 'ltd', 'inc', 'lp', 'ilp', 'no', 'liability', 'nl', 'proprietary', 'pty', 'corporation', 'indigenous', 'rntbc', 'sce', 'keg', 'gesmbh', 'gmbh', 'eu', 'ag', 'ohg', 'og', 'oeg', 'se', 'kg', 'kgaamsz', 'gbhsz', 'ages', 'unp', 'guhsz', 'ewiv', 'genmbh', 'eog', 'ohgmsz', 'pgmbhma', 'gvorp', 'orvohgza', 'gmuhgb', 'wiv', 'pmbhsz', 'kgaa', 'zrg', 'gar', 'genmubh', 'ekg', 'pgmbh', 'wivmsz', 'zvggbh', 'pgbhsz', 'oe', 'o', 'rag', 'lg', 'ivog', 'zvgpgbh', 'vog', 'zvggugch', 'ofrgmbh', 'ekgmsz', 'prst', 'ofp', 'agmsz', 'gns', 'fs', 'sca', 'scrl', 'ent', 'e', 'epp', 'scri', 'geie', 'isbl', 'snc', 'sprlu', 'saspj', 'dpu', 'asbl', 'cp', 'gie', 'sprl', 'sc', 'sdc', 'scs', 'etspubli', 'sa', 'sagr', 'aisbl', 'fondpriv', 's', 'agr', 'fup', 'so', 'cva', 'cvba', 'bo', 'onp', 'cvoa', 'eesv', 'izw', 'ebvba', 'vvzrl', 'pr', 'vzw', 'cd', 'esv', 'bvba', 'ms', 'commv', 'oi', 'gcv', 'commva', 'lv', 'ivzw', 'gcw', 'priv', 'st', 'son', 'ет', 'еад', 'с', 'ие', 'кда', 'адсиц', 'кд', 'ед', 'дззд', 'екд', 'оод', 'ад', 'еоод', 'srl', 'llp', 'sencrl', 'corp', 'pc', 'company', 'loan', 'trustco', 'trustee', 'trust', 'ltee', 'limitee', 'union', 'condominium', 'partnership', 'incorporated', 'by', 'guarantee', 'society', 'association', 'communautaire', 'cic', 'sic', 'interest', 'interet', 'community', 'societe', 'd', 'ulc', 'trustees', 'fiduciaires', 'manitoba', 'incorporee', 'a', 'responabilite', 'pool', 'parish', 'catholic', 'paroisse', 'catholique', 'ukrainienne', 'ukrainian', 'commandite', 'en', 'sarf', 'pret', 'compagnie', 'de', 'fiduciaire', 'fiducie', 'cer', 'cooperation', 'cooperatif', 'sec', 'senc', 'giu', 'egiu', 'tp', 'jtd', 'dd', 'kd', 'jdoo', 'doo', 'ivs', 'i', 'p', 'selskab', 'smba', 'aps', 'k', 'amba', 'eøfg', 'fmba', 'fie', 'hu', 'ku', 'as', 'tu', 'au', 'ou', 'emhu', 'uu', 'mtu', 'tuh', 'vvag', 'mbb', 'partg', 'ug', 'ek', 'ev', 'eg', 'eeig', 'ptc', 'plc', 'ee', 'epe', 'sp', 'other', 'pl', 'slp', 'jv', 'ike', 'clf', 'jso', 'fdn', 'unltd', 'ultd', '有限公司', '無限公司', 'nyrt', 'zrt', 'rt', 'kht', 'kkt', 'kft', 'bt', 'kbe', 'hsz', 'tksz', 'oba', 'slhf', 'slf', 'hf', 'ehf', 'icav', 'dac', '–', 'clg', 'uc', 'pulc', 'shares', 'puc', 'i&ps', 'cga', 'ctr', 'cn', 'teo', 'cti', 'cpt', 'ss', 'el', 'ed', 'ge', 'fi', 'rs', 'sg', 'sl', 'cf', 'at', 'rc', 'll', 'ei', 'di', 'oc', 'sr', 'sn', 'sm', 'cm', 'sd', 'ma', 'cz', 'ep', 'sv', 'l', 'arl', 'ks', 'ps', 'ik', 'sia', 'reg', 'egen', 'eb', 'vi', 'ekb', 'apb', 'ab', 'rb', 'ii', 'uab', 'tub', 'lpra', 'tr', 'lf', 'bn', 'bi', 'vs', 'ko', 'kb', 'pdb', 'per', 'etbg', 'crc', 'mb', 'zub', 'cb', 'pp', 'si', 'assep', 'am', 'secs', 'aa', 'seca', 'sepcav', 'sicaf', 'aam', 'sarl', 'oth', 'sci', 'secsp', 'sicav', 'fon', 'pt', 'f', 'ste', 'cv', 'owm', 'io', 'rp', 'vve', 'cooperatie', 'ans', 'kf', 'nuf', 'sf', 'fkf', 'bbl', 'da', 'enk', 'asa', 'brl', 'ba', 'iks', 'pvt', 'smc', 'unlimited', 'spp', 'sj', 'spk', 'oo', 'z', 'ska', 'ofe', 'tuw', 'kda', 'ad', 'siz', 'ong', 'pfi', 'ra', 'pfa', 'af', 'дп', 'пр', 'јп', 'доо', 'од', 'pte', 'csd', 'specorgjednotka', 'jednotzelspravuradu', 'zahranicosoba', 'pravnicka', 'spol', 'akc', 'zastuporginych', 'statov', 'ver', 'obch', 'shr', 'rolnik', 'v', 'or', 'zastupzahrpravosoby', 'jedzboru', 'zel', 'ochrany', 'druzstevny', 'podnik', 'pol', 'hn', 'orgjednpolstrany', 'social', 'zdravpoistovna', 'ziv', 'slobpovolanie', 'fo', 'polnohospodardruzstvo', 'jednstatzeltechins', 'zavod', 'poistovne', 'oblast', 'zivnostnik', 'stathosporgriadokr', 'jednoducha', 'akcie', 'na', 'medzinar', 'org', 'zdruz', 'fyzicka', 'orgjednotka', 'zdruzenia', 'zaujorgdruz', 'spolocna', 'rdis', 'ine', 'skoly', 'pracvysokej', 'ucelova', 'zahr', 'obchorg', 'poistovna', 'banka', 'statpenazustav', 'dochodpoist', 'doplnkova', 'osoby', 'zlozka', 'alebo', 'hospzar', 'kom', 'zdruzmedzinarobchodu', 'obec', 'murad', 'mesto', 'odstepny', 'samostatne', 'podnikajuca', 'prisporg', 'orgzlozka', 'pobocka', 'statpenazust', 'jedn', 'prevadzkaren', 'samost', 'pravosob', 'zaujm', 'slpovolanie', 'ziva', 'nbs', 'orgdruzstiev', 'zaujmova', 'svojpomocpolndruzstvo', 'ina', 'orgverejnej', 'spravy', 'oblorgjednotka', 'europzoskupuzemspol', 'neziskorgposkytvseobprospsluzby', 'infstrediska', 'zahrkul', 'r', 'pzo', 'zahrmajuc', 'verejnopravinstitucia', 'europzoskuphospzaujm', 'zdruzfyzosob', 'zaujmove', 'spolocenstva', 'vlastnikov', 'dno', 'kdd', 'cc', 'npc', 'soc', 'srll', 'sll', 'scoop', 'scp', 'srcp', 'sii', 'slne', 'mps', 'sap', 'scr', 'scoopp', 'aeie', 'pyme', 'fiamm', 'fp', 'scom', 'scom:pap', 'aie', 'sgr', 'erl', 'srlp', 'fcr', 'iic', 'fii', 'sal', 'src', 'c', 'com', 'fim', 'scomp', 'tsf', 'hb', 'bab', 'for', 'sb', 'fof', 'ofb', 'fab', 'khf', 'egts', 'brf', 'gen', 'ausl', 'botschaft', 'gesellsch', 'einfache', 'rechtsform', 'bund', 'inst', 'recht', 'off', 'einzelfirma', 'unt', 'kommanditgesellsch', 'organisation', 'int', 'rechtl', 'korp', 'kanton', 'gemeinde', 'prokura', 'kollektivgesellsch', 'aus', 'kommandit', 'kapitalanlagen', 'hr', 'zweig', 'bezirk', 'foreign', 'ltdco', 'embassy', 'simple', 'legal', 'nature', 'federal', 'administration', 'pub', 'individually', 'owned', 'fed', 'publ', 'internat', 'public', 'cantonal', 'local', 'cant', 'att', 'power', 'loc', 'general', 'undivided', 'enterprise', 'part', 'coll', 'invest', 'branch', 'distr', 'district', 'etranger', 'ambassade', 'etran', 'jur', 'confederation', 'droit', 'raison', 'individuelle', 'federale', 'internationales', 'canton', 'commune', 'cantonale', 'sadom', 'procuration', 'communale', 'corpor', 'collectif', 'nom', 'indivisions', 'etrangere', 'investissement', 'succ', 'action', 'comm', 'estero', 'sagl', 'ambasciate', 'estera', 'natura', 'guiri', 'confederazione', 'pubblico', 'dir', 'ist', 'individuale', 'ragione', 'imp', 'pubb', 'accomandita', 'in', 'internazionali', 'diritto', 'cantone', 'comune', 'dom', 'procura', 'comunale', 'corpora', 'collettivo', 'nome', 'indivisioni', 'str', 'investimenti', 'distretto', 'azioni', 'kollsti', 'komsti', 'sti', 'ccc', 'cyf', 'pac', 'br', 'pllc', 'electric', 'membership', 'emc', 'l3c', 'ssb', 'registered', 'rllp', 'llc', 'lllp', 'rlllp', 'pll', 'having', 'assn', 'chtd', 'lca', 'assoc', 'lc', 'et', 'coop', 'ead', 'ie', 's', 'sd', 'kda', 'adsic', 'kd', 'dzzd', 'ood', 'ad', 'eood', 'cooperation', 'cooperative', 'corp', 'ltd', 'inc', 'dp', 'pr', 'jp', 'doo', 'od', 'business', 'international', 'corporation', 'stichting', 'vennootschap', 'onder', 'firma', 'commanditaire', '1', 'besloten', 'vereniging', 'naamloze', 'cooperatieve', 'eenmanszaak', 'vrijgestelde', 'aruba', 'recht', 'buitenlands', 'maatschap', 'beperkte', 'met', 'aansprakelijkheid', '1+', 'operative', 'co', 'association', 'incorporated', 'partnership', 'limited', 'by', 'public', 'company', 'guarantee', 'no', 'liability', 'proprietary', 'unlimited', 'shares', 'indigenous', 'rechtstrager', 'sonstiger', 'privatstiftung', 'genossenschaft', 'europaische', 'sce', 'kommandit', 'erwerbsgesellschaft', 'mit', 'haftung', 'gesellschaft', 'beschrankter', 'auf', 'versicherungsverein', 'gegenseitigkeit', 'interessenvereinigung', 'wirtschaftliche', 'einzelunternehmer', 'aktiengesellschaft', 'einzelkaufmann', 'offene', 'handelsgesellschaft', 'sparkasse', 'erwerbs', 'und', 'wirtschaftsgenossenschaft', 'se', 'kommanditgesellschaft', 'sozialer', 'zielsetzung', 'aktien', 'europaea', 'societas', 'auslandische', 'naturliche', 'person', 'unternehmen', 'unbeschrankter', 'einrichtung', 'gewinnerzielungsabsicht', 'ohne', 'alleingesellschafter', 'privatgesellschaft', 'einem', 'oder', 'rechtspersonlichkeit', 'gesellschaften', 'vereinigungen', 'rechtliche', 'offentlich', 'vereinigung', 'beteiligung', 'rechtsform', 'zivilrechtliche', 'einer', 'in', 'der', 'rechts', 'allgemeinen', 'des', 'einfache', 'offentliche', 'einfachen', 'offenen', 'landwirtschaftlichen', 'internationale', 'landwirtschaftliche', 'gemeinnutzige', 'stiftung', 'commandite', 'finalite', 'sociale', 'actions', 'societe', 'cooperative', 'responsabilite', 'limitee', 'europeenne', 'entreprise', 'etrangere', 'physique', 'personne', 'illimitee', 'economique', 'groupement', 'europeen', 'interet', 'lucratif', 'but', 'sans', 'institution', 'nom', 'collectif', 'unipersonnelle', 'privee', 'personnalite', 'juridique', 'droit', 'participation', 'civile', 'sous', 'forme', 'commun', 'simple', 'etablissement', 'anonyme', 'agricole', 'fondation', 'publique', 'utilite', 'oogmerk', 'op', 'sociaal', 'aandelen', 'een', 'europese', 'buitenlandse', 'onderneming', 'persoon', 'natuurlijk', 'onbeperkte', 'europees', 'economisch', 'samenwerkingsverband', 'instelling', 'winstoogmerk', 'zonder', 'eenpersoons', 'of', 'rechtspersoonlijkheid', 'publiek', 'van', 'wijze', 'bij', 'deelneming', 'burgerlijke', 'vorm', 'gewone', 'openbare', 'landbouwvennootschap', 'bv', 'lv', 'private', 'nut', 'openbaar', 'nederlands', 'naar', 'meerdere', 'vennoten', 'beherende', 'rechtsbevoegdheid', 'aandeelhouder', 'bestuurde', 'particulier', 'fonds', 'hoofdvestiging', 'buiten', 'bonaire', 'nevenvestiging', 'volledige', 'eigenaren', 'rechtsvorm', 'cooperatie', 'beherend', 'vennoot', 'close', 'companies', 'едноличен', 'търговец', 'кооперация', 'акционерно', 'дружество', 'еднолично', 'съдружие', 'събирателно', 'сд', 'командиртно', 'акции', 'с', 'инвестиционна', 'със', 'специална', 'цел', 'европеиско', 'задълженията', 'договорите', 'за', 'закона', 'и', 'учредено', 'по', 'кооперативно', 'отговорност', 'ограничена', 'trade', 'name', 'sole', 'proprietorship', 'trust', 'alberta', 'utility', 'rural', 'professional', 'loan', 'union', 'society', 'general', 'act', 'non', 'profit', 'corp', 'agricultural', 'religious', 'service', 'includes', 'housing', 'community', 'outside', 'bc', 'formed', 'fund', 'pension', 'fire', 'mutual', 'insurance', 'extraprovincial', 'share', 'registered', 'foreign', 'entity', 'funded', 'member', 'contribution', 'board', 'parliament', 'corporations', 'enacted', 'capital', 'without', 'fair', 'condominium', 'project', 'new', 'brunswick', 'proprietor', 'depends', 'on', 'legislature', 'unions', 'condominiums', 'not', 'operatives', 'for', 'ns', 'partnerships', 'holding', 'investment', 'interest', 'names', 'proprietors', 'ontario', 'legislative', 'assembly', 'v', 'part', 'under', 'which', 'liabilty', 'saskatchewan', 'generation', 'syndicates', 'ventures', 'joint', 'recreation', 'including', 'lawyers', 'accountants', 'extra', 'provincial', 'only', 'manitoba', 'parish', 'catholic', 'ukrainian', 'registration', 'territorial', 'nt', 'authorized', 'commerce', 'chambre', 'parlement', 'constituee', 'loi', 'organisation', 'retraite', 'professionnelle', 'compagnie', 'pret', 'nouveau', 'selon', 'condominiale', 'fiducie', 'gerant', 'projet', 'morale', 'residante', 'agricoles', 'foires', 'unique', 'appellation', 'commerciale', 'proprietaire', 'cooperatif', 'syndicat', 'quebec', 'caractere', 'speciale', 'trois', 'colomb', 'federation', 'colleges', 'services', 'concernant', 'etablissements', 'conservation', 'cruaute', 'commissions', 'partie', 'sociaux', 'jean', 'peche', 'marche', 'certaines', 'territoires', 'cimetieres', 'produits', 'clubs', 'eveques', 'faune', 'iii', 'detention', 'decrets', 'professionnels', 'cris', 'animaux', 'habitation', 'cooperatives', 'regionale', 'fabriques', 'saint', 'cimetiere', 'catholiques', 'urbanisme', 'chasse', 'administration', 'scolaires', 'autochtones', 'guides', 'bienfaisance', 'territoriale', 'laitieres', 'securite', 'associations', 'baptiste', 'certains', 'chevaliers', 'agriculture', 'professionnelles', 'œuvre', 'instruction', 'enseignement', 'compagnies', 'travail', 'nordiques', 'sante', 'cercles', 'rivieres', 'syndicats', 'province', 'religieuses', 'municipale', 'envers', 'constitution', 'probation', 'nationales', 'mise', 'code', 'qualification', 'horticulture', 'romains', 'valeur', 'amenagement', 'formation', 'minieres', 'kativik', 'scouts', 'main', 'villages', 'ii', 'eglises', 'alimentaires', 'collective', 'pour', 'assurances', 'preventives', 'professions', 'correctionnels', 'regroupement', 'group', 'miniers', 'villes', 'gestion', 'societes', 'professionnel', 'convention', 'cites', 'epargne', 'eau', 'patrons', 'mutuel', 'constitue', 'flottage', 'quebecoise', 'acte', 'developpement', 'entraide', 'miniere', 'gaz', 'electricite', 'laitiers', 'elevage', 'fideicommis', 'producteurs', 'telephone', 'exploration', 'construction', 'telegraphe', 'copropriete', 'prive', 'kreditna', 'unija', 'interesno', 'gospodarsko', 'udruzenje', 'skraceno', 'europsko', 'egiu', 'zadruga', 'cooperativa', 'europska', 'trgovac', 'pojedinac', 'drustvo', 'masa', 'stecajna', 'zadruge', 'savez', 'trgovacko', 'javno', 'dionicko', 'komanditno', 'podruznica', 's', 'odgovornoscu', 'jednostavno', 'ogranicenom', 'zajednica', 'ustanova', 'stille', 'rederij', 'onderlinge', 'waarborgmaatschappij', 'νομικη', 'μορφη', 'αλλη', 'συνεταιρισμοσ', 'δημοσια', 'ευθυνησ', 'ευρωπαικη', 'εταιρεια', 'περιορισμενησ', 'με', 'μετοχεσ', 'επωνυμια', 'eμπορικη', 'σωματεια', 'ιδρυματα', 'και', 'αλλοδαπη', 'αυτοτελωσ', 'εργαζομενοσ', 'εχει', 'κεφαλαιο', 'μετοχικο', 'εγγυηση', 'που', 'ιδιωτικη', 'προνοιασ', 'συνταξεωσ', 'ταμεια', 'οντοτητεσ', 'διεπονται', 'δημοσιο', 'απο', 'δικαιο', 'το', 'πιστωτικα', 'συνεργατικα', 'χωρισ', 'svepomocne', 'zemedelske', 'druzstvo', 'zarizeni', 'strany', 'nebo', 'podnik', 'hospodarske', 'politicke', 'konsolidacni', 'ceska', 'agentura', 'evropske', 'pro', 'spolupraci', 'seskupeni', 'uzemni', 'nadace', 'fond', 'zakona', 'ze', 'statni', 'zajmova', 'druzstev', 'organizace', 'regionalni', 'rada', 'soudrznosti', 'regionu', 'cennymi', 'papiry', 'obchodniku', 'garancni', 'staly', 'rozhodci', 'soud', 'zamestnavatelu', 'pobocna', 'mezinarodni', 'verejna', 'obchodni', 'spolecnost', 'akciova', 'sdruzeni', 'organizacni', 'jednotka', 'obcanskeho', 'na', 'komanditni', 'akcie', 'ostatni', 'prispevkova', 'zajmove', 'hospodarska', 'uradem', 'rizena', 'okresnim', 'spotrebni', 'tiskova', 'kancelar', 'tuzemska', 'fyzicka', 'osoba', 'podnikajici', 'rucenim', 'omezenym', 'obcanske', 'do', 'nezapisujici', 'rejstriku', 'obchodniho', 'zeleznicni', 'cesty', 'sprava', 'dopravni', 'prospesna', 'obecne', 'zdravotni', 'vseobecna', 'pojistovna', 'drobna', 'uradu', 'obecniho', 'provozovna', 'samostatna', 'vyrobni', 'spolek', 'ucasti', 'majetkovou', 'zahranicni', 'instituce', 'vyzkumna', 'skolska', 'pravnicka', 'cirkvi', 'spolecnosti', 'a', 'svazy', 'nabozenskych', 'ustav', 'penezni', 'banka', 'cirkve', 'nabozenske', 'pobocny', 'neziskove', 'verejne', 'ustavni', 'zdravotnicke', 'agrarni', 'komora', 'statu', 'slozky', 'vnitrni', 'obchodu', 'zahranicniho', 'slozka', 'nadacniho', 'fondu', 'mezinarodniho', 'zvlastni', 'organizacich', 'mezinarodnich', 'zastoupeni', 'zajmu', 'nevladnich', 'ceskych', 'jednotek', 'spolecenstvi', 'vlastniku', 'obec', 'evidovane', 'osoby', 'pravnicke', 'cirkevni', 'ceskoslovenska', 'honebni', 'spolecenstvo', 'ceskoslovenske', 'drahy', 'odborova', 'obci', 'dobrovolny', 'svazek', 'samospravnym', 'uzemnim', 'zrizena', 'celkem', 'verejnopravni', 'vice', 'zakladateli', 'spolecny', 'narodni', 'komoditni', 'burza', 'samospravna', 'stavovska', 'profesni', 'vysoka', 'skola', 'mestska', 'cast', 'obvod', 'mestsky', 'nevladni', 'kraj', 'verejny', 'auditem', 'nad', 'dohled', 'mimo', 'vzp', 'nadacni', 'zakladatelem', 'druzstevni', 'obecni', 'evropska', 'bytove', 'odstepny', 'zavod', 'fyzicke', 'spolecna', 'osob', 'pravnickych', 'zemedelsky', 'ucelova', 'zahranicne', 'verejneho', 'zakonem', 'pravnikca', 'zapisovana', 'zvlastnim', 'strana', 'politicka', 'hnuti', 'jine', 'iværksætterselskab', 'interessentskab', 'partnerselskab', 'enkeltmandsvirksomhed', 'andelsselskab', 'europæisk', 'begrænset', 'med', 'ansvar', 'selskab', 'anpartsselskab', 'medarbejderinvesteringsselskab', 'kommanditselskab', 'firmagruppe', 'økonomisk', 'forening', 'aktieselskab', 'sihtasutus', 'isikust', 'fuusilisest', 'ettevotja', 'hooneuhistu', 'ariuhing', 'euroopa', 'korteriuhistu', 'aktsiaselts', 'usuline', 'uhendus', 'erakond', 'taisuhing', 'ametiuhing', 'osauhing', 'majandushuviuhing', 'usaldusuhing', 'loomeliit', 'mittetulundusuhing', 'uhistu', 'tulundusuhistu', 'collectivite', 'regie', 'locale', 'administratif', 'scp', 'medecins', 'salaries', 'autre', 'nationale', 'conseil', 'personnes', 'physiques', 'creee', 'entre', 'fait', 'sarl', 'attribution', 'entente', 'interregionale', 'etranger', 'etat', 'directoire', 'mutuelle', 'materiel', 'utilisation', 'cuma', 'simplifiee', 'exercice', 'liberal', 'action', 'registre', 'inscrite', 'notaires', 'incendie', 'secours', 'sdis', 'departemental', 'consommation', 'local', 'declaree', 'specialise', 'cooperation', 'autorisee', 'syndicale', 'hlm', 'liberale', 'profession', 'petr', 'equilibre', 'pole', 'foncier', 'prevoyance', 'commercant', 'social', 'medico', 'sai', 'supplementaire', 'sas', 'experts', 'geometres', 'financieres', 'spfpl', 'participations', 'maritime', 'geie', 'sica', 'veterinaires', 'forestier', 'dote', 'territoire', 'mer', 'outre', 'deconcentre', 'competence', 'inter', 'departementale', 'safer', 'juridiques', 'conseils', 'commune', 'deleguee', 'associee', 'regime', 'hors', 'defense', 'ministere', 'vente', 'immobiliere', 'assurance', 'mixte', 'economie', 'equipement', 'urbain', 'district', 'urbaine', 'fonciere', 'architectes', 'ouvriere', 'constitutionnelle', 'autorite', 'artisanale', 'exploitation', 'immobilier', 'infirmiers', 'investissement', 'paroisse', 'zone', 'concordataire', 'ensemble', 'mutualite', 'liberales', 'artisan', 'region', 'vocation', 'intercommunal', 'sivom', 'multiple', 'organisme', 'mutualiste', 'insertion', 'federale', 'production', 'secteur', 'industriel', 'centre', 'technique', 'comite', 'scop', 'national', 'commercial', 'comptable', 'appel', 'avoues', 'sicomi', 'industrie', 'immatricule', 'agence', 'rcs', 'representation', 'fonction', 'centrale', 'ayant', 'nouvelle', 'comptes', 'commissaires', 'smia', 'soins', 'ambulatoires', 'interprofessionnelles', 'assimile', 'ordre', 'commercants', 'detaillants', 'cias', 'greffiers', 'tribunal', 'transport', 'municipal', 'intermediaire', 'haut', 'bas', 'moselle', 'rhin', 'sivu', 'avocats', 'priseurs', 'laitiere', 'hospitalier', 'dentistes', 'communes', 'biens', 'commission', 'indivis', 'scientifique', 'culturel', 'propriete', 'progressive', 'accession', 'cercle', 'armees', 'dans', 'foyer', 'patronal', 'masseurs', 'kinesitherapeutes', 'special', 'associe', 'moyens', 'interdepartementale', 'alsace', 'agglomeration', 'communaute', 'pas', 'dependant', 'vieillesse', 'ne', 'ferme', 'banque', 'communal', 'remembrement', 'avec', 'indivision', 'congregation', 'metropole', 'immatriculee', 'gaec', 'consulaire', 'gie', 'sanitaire', 'sca', 'agent', 'chomage', 'ecoles', 'exploitant', 'ophlm', 'loyer', 'office', 'modere', 'caution', 'ecole', 'dotee', 'medicale', 'directeurs', 'laboratoire', 'analyse', 'central', 'hospitalisation', 'maladie', 'indication', 'sicav', 'variable', 'employeurs', 'huissiers', 'reconnue', 'section', 'departement', 'administrative', 'independante', 'metropolitain', 'officier', 'ministeriel', 'complementaire', 'scpi', 'placement', 'gip', 'pastoral', 'individuelle', 'ouvert', 'libre', 'lorraine', 'cultes', 'berufshaftung', 'partnerschaftsgesellschaft', 'unternehmergesellschaft', 'kaufmann', 'eingetragener', 'verein', 'external', 'subsidiary', 'economic', 'european', 'groupings', 'foundations', 'europeas', 'εταιρια', 'ναυτικη', 'ετερορρυθμη', 'αστικη', 'προσωπικη', 'λοιπα', 'δημοσιου', 'δικαιου', 'νομικα', 'προσωπα', 'αφανησ', 'κοινοπραξια', 'κεφαλαιουχικη', 'ομορρυθμη', 'κατα', 'συμπλοιοκτησια', 'ανωνυμη', 'foundation', 'partnertship', 'trustee', 'ordinance', 'established', 'kong', 'hong', 'with', '私人股份有限公司', '註冊受託人', '根據法例成立的實體', '公眾股份有限公司', '非香港公司', '有股本的公眾無限公司', '擔保有限公司', '有股本的私人無限公司', '有限責任合夥', 'koztestulet', 'egyeb', 'egyesulet', 'reszvenytarsasag', 'mukodo', 'nyilvanosan', 'befektetesi', 'alap', 'magannyugdijpenztar', 'zartkoruen', 'alapitvany', 'kolcsonos', 'biztosito', 'szovetkezet', 'tarsasag', 'kozhasznu', 'kozkereseti', 'onkentes', 'biztositopenztar', 'vallalkozas', 'kepviselete', 'kereskedelmi', 'kulfoldi', 'szekhelyu', 'korlatolt', 'felelossegu', 'beteti', 'szemelyisegu', 'nem', 'sorolt', 'jogi', 'mashova', 'szovetseg', 'kiveve', 'sportszovetseg', 'fioktelepe', 'hitelszovetkezet', 'takarek', 'es', 'europai', 'orszagos', 'betetbiztositasi', 'samlagshlutafelag', 'samlagsfelag', 'evropufelag', 'hlutafelag', 'einkahlutafelag', 'irish', 'vehicle', 'asset', 'management', 'grouping', 'friendly', 'designated', 'dac', 'activity', '–', 'that', 'has', 'ltd', 'provident', 'industrial', 'ainmnithe', 'ghniomhaiochta', 'cuideachta', 'theorainn', 'rathaiochta', 'faoi', 'neamhtheoranta', 'teoranta', 'infheistiochta', 'comhphairtiocht', 'theoranta', 'phoibli', 'having', '1931', '2006', 'personality', 'legal', 'building', 'altro', 'stato', 'leggi', 'base', 'di', 'societa', 'costituita', 'ente', 'semplice', 'pubblico', 'diritto', 'europeo', 'gruppo', 'economico', 'interesse', 'impresa', 'fondazione', 'responsabilita', 'semplificata', 'limitata', 'europea', 'consortile', 'fidi', 'consorzio', 'autonoma', 'statale', 'azienda', 'rete', 'giuridica', 'contratto', 'dotato', 'soggettivita', 'dlgs', 'al', '267', '2000', 'cui', 'individuale', 'azioni', 'per', 'nome', 'collettivo', 'mutuo', 'soccorso', 'mutua', 'assicurazione', 'alla', 'professionisti', 'tra', 'separate', 'komanditsabiedriba', 'pilnsabiedriba', 'komercsabiedriba', 'eiropas', 'komersants', 'individualais', 'ierobezotu', 'ar', 'atbildibu', 'sabiedriba', 'akciju', 'treuunternehmen', 'kollektivgesellschaft', 'anstalt', 'europos', 'bendroves', 'valstybes', 'imones', 'kooperatines', 'bendrijos', 'advokatu', 'profesines', 'seimynos', 'ir', 'susivienijimai', 'sajungos', 'ju', 'akcines', 'centrai', 'bendruomenes', 'religines', 'individualios', 'ekonominiu', 'interesu', 'grupes', 'uzdarosios', 'ukines', 'tikrosios', 'rumu', 'lietuvos', 'prekybos', 'asociacija', 'pramones', 'amatu', 'tradicines', 'asociacijos', 'labdaros', 'fondai', 'paramos', 'istaigos', 'biudzetines', 'viesosios', 'kooperatyvai', 'komanditines', 'detektyvu', 'privaciu', 'rumai', 'institucijos', 'nuolatines', 'arbitrazo', 'sodininku', 'bendradarbiavimo', 'teritorinio', 'pranesimu', 'centras', 'valdymo', 'bendras', 'mazosios', 'zemes', 'ukio', 'centrinis', 'bankas', 'politines', 'partijos', 'savivaldybiu', 'momentanee', 'fixe', 'mutuelles', 'entreprises', '19', 'autres', 'societesdes', '2002', 'morales', 'dont', 'immatriculation', 'modifiee', 'article', 'est', 'prevue', 'decembre', 'commendite', 'en', 'akkomandita', 'jew', 'socjeta', 'pubblika', 'kumpanija', 'kollettiv', 'f', 'isem', 'privata', 'companiy', 'bodies', 'parastal', 'ministries', 'others', 'rechtspersoon', 'publiekrechtelijke', 'oprichting', 'eigenaars', 'gemene', 'voor', 'rekening', 'kerkgenootschap', 'selskap', 'ansvarlig', 'stiftelse', 'foretak', 'kommunalt', 'norskregistrert', 'utenlandsk', 'statsforetak', 'fylkeskommunalt', 'gjensidig', 'forsikringsselskap', 'boligbyggelag', 'partsrederi', 'pensjonskasse', 'delt', 'foretaksgruppe', 'europeisk', 'enkeltpersonforetak', 'forening?', 'innretning', 'bare', 'eller', 'lag', 'juridisk', 'annen', 'allmennaksjeselskap', 'samvirkeforetak', 'verdipapirfond', 'kommandittselskap', 'borettslag', 'konkursbo', 'begrenset', 'sparebank', 'aksjeselskap', 'interkommunalt', 'eierseksjonssameie', 'multi', 'single', 'unlisted', 'listed', 'samodzielne', 'opieki', 'zakłady', 'publiczne', 'zdrowotnej', 'społki', 'partnerskie', 'izby', 'cechy', 'rzemieslnicze', 'i', 'gospodarcze', 'administracji', 'kontroli', 'oraz', 'prawa', 'trybunały', 'ochrony', 'rzadowej', 'organy', 'panstwowej', 'sady', 'władzy', 'jawne', 'zagranicznego', 'oddział', 'reasekuracji', 'zakładu', 'głowny', 'zrzeszenia', 'społdzielnie', 'fundacje', 'samorzadowe', 'organizacyjne', 'jednostki', 'komandytowe', 'gospodarki', 'budzetowej', 'instytucje', 'wzajemnej', 'towarzystwa', 'panstwa', 'skarb', 'rolnicze', 'kołka', 'akcyjne', 'zawodowe', 'społeczne', 'organizacje', 'mieszkaniowe', 'wspolnoty', 'społdzielcze', 'kasy', 'kredytowe', 'oszczednosciowo', 'polityczne', 'społka', 'europejska', 'panstwowe', 'badawcze', 'instytuty', 'zwiazki', 'odpowiedzialnoscia', 'ograniczona', 'z', 'komandytowo', 'ubezpieczen', 'fundusze', 'emerytalne', 'otwarte', 'systemu', 'placowki', 'oswiaty', 'inwestycyjne', 'przedsiebiorcy', 'przedsiebiorstwa', 'koscioły', 'wyznaniowe', 'inne', 'niz', 'wzajemnych', 'uczelnie', 'cywilne', 'działalnosc', 'prowadzace', 'fizyczne', 'gospodarcza', 'stowarzyszen', 'stowarzyszenia', 'financeira', 'exterior', 'sucursal', 'de', '2o', 'grau', 'permanente', 'representacao', 'intermunicipal', 'entidade', 'empresarial', 'fundo', 'europeu', 'agrupamento', 'publica', 'associacao', 'anonima', 'sociedade', 'empresa', 'organismo', 'administracao', 'da', 'europeia', 'em', 'coletivo', 'metropolitana', 'comandita', 'publico', 'coletiva', 'direito', 'pessoa', 'internacional', 'por', 'quotas', 'unipessoal', 'desportiva', 'complementar', 'empresas', 'fundacao', 'responsabilidade', 'limitada', 'estabelecimento', 'individual', 'regional', 'со', 'друштво', 'командитно', 'акционерско', 'трговско', 'претпријатие', 'јавно', 'интересна', 'заедница', 'стопанска', 'одговрност', 'подрушница', 'на', 'односно', 'странски', 'странско', 'трговрец', 'поединец', 'трговец', 'societate', 'europeana', 'mestesugareasca', 'interes', 'grupul', 'organizatie', 'guvernamentala', 'ale', 'si', 'casele', 'organizatii', 'cooperatiste', 'acestora', 'reprezentanta', 'consum', 'fizica', 'independenta', 'persoana', 'pe', 'actiuni', 'proprietate', 'alte', 'intreprindere', 'individuala', 'agricola', 'nume', 'colectiv', 'autorizata', 'sucursala', 'reprezentant', 'fiscal', 'familiala', 'asociatie', 'simpla', 'raspundere', 'cu', 'ассоциации', 'объединения', 'организации', 'благотворительных', 'союзы', 'общества', 'ответственностью', 'ограниченнои', 'фермерские', 'крестьянские', 'хозяиства', 'автономные', 'некоммерческие', 'учреждения', 'благотворительные', 'общественных', 'объединении', 'кооперативов', 'муниципальные', 'собственников', 'жилья', 'товарищества', 'казенные', 'федеральные', 'предприятия', 'кооперативы', 'сельскохозяиственные', 'производственные', 'кроме', 'сельскохозяиственных', 'производственных', 'профсоюзные', 'коммерческими', 'лица', 'организациями', 'являющиеся', 'прочие', 'юридические', 'россиискои', 'субъектом', 'федерации', 'созданные', 'акционерные', 'публичные', 'адвокаты', 'учредившие', 'адвокатскии', 'кабинет', 'потребительские', 'животноводческие', 'или', 'жилищные', 'жилищно', 'строительные', 'академии', 'государственные', 'наук', 'бюджетные', 'субъектов', 'дачные', 'огороднические', 'садоводческие', 'правовые', 'публично', 'компании', 'образовании', 'муниципальных', 'советы', 'унитарные', 'бюро', 'адвокатские', 'казачьи', 'реестр', 'обществ', 'государственныи', 'казачьих', 'в', 'внесенные', 'кредитные', 'гаражные', 'гаражно', 'для', 'деятельности', 'формы', 'лиц', 'граждан', 'физических', 'организационно', 'некоммерческими', 'являющихся', 'корпоративными', 'юридических', 'огороднических', 'садоводческих', 'некоммерческих', 'дачных', 'партнерства', 'фонды', 'проката', 'экологические', 'общественные', 'корпорации', 'коммерческои', 'артели', 'самоуправления', 'территориальные', 'федерациеи', 'общины', 'малочисленных', 'коренных', 'народов', 'подразделения', 'обособленных', 'структурные', 'подразделении', 'недвижимости', 'второго', 'уровня', 'палаты', 'религиозные', 'обслуживающие', 'перерабатывающие', 'унитарными', 'снабженческие', 'колхозы', 'саморегулируемые', 'вере', 'коммандитные', 'простые', 'без', 'юридического', 'созданных', 'прав', 'непубличные', 'хозяиственные', 'хозяиств', 'главы', 'фермерских', 'крестьянских', 'самодеятельности', 'органы', 'общественнои', 'отделения', 'неправительственных', 'иностранных', 'политические', 'партии', 'сбытовые', 'торговые', 'представительства', 'основанные', 'праве', 'оперативного', 'управления', 'индивидуальные', 'предприниматели', 'экономического', 'взаимодеиствия', 'нотариальные', 'международные', 'межправительственные', 'муниципальным', 'образованием', 'страхования', 'взаимного', 'осуществляющих', 'международных', 'территории', 'деятельность', 'частнои', 'практикои', 'нотариусы', 'занимающиеся', 'хозяиственного', 'ведения', 'работодателеи', 'не', 'к', 'предпринимательству', 'отнесеннои', 'потребительских', 'коллегии', 'адвокатов', 'городские', 'суды', 'межраионные', 'раионные', 'рыболовецкие', 'обособленные', 'филиалы', 'накопительные', 'кредитных', 'неправительственные', 'кооперативные', 'коопхозы', 'общин', 'частные', 'инвестиционные', 'паевые', 'движения', 'негосударственные', 'пенсионные', 'торгово', 'промышленные', 'полные', 'charitable', 'overseas', 'савез', 'задружни', 'друштвено', 'предузеће', 'предузетник', 'задруга', 'одговорношћу', 'ограниченом', 'са', 'акционарско', 'ортачко', 'branch', 'organizacie', 'rozpoctove', 'prispevkove', 'organizacna', 'csd', 'specializovana', 'obecny', 'spravneho', 'zeleznicneho', 'rozpoctova', 'organizacia', 'sidlom', 'so', 'zahranicna', 'sr', 'uzemia', 'spolocnost', 'statny', 'oddieli', 'psn', 'komoditna', 'jednym', 'druzstevny', 'zakladatelom', 'sporitelne', 'pobocka', 'urad', 'krajsky', 'vybor', 'narodny', 'zastupitelske', 'inych', 'statov', 'obchodna', 'profesna', 'rolnik', 'hospodariaci', 'obchodnom', 'samostatne', 'registri', 'zapisany', 'nezapisany', 'stredna', 'samospravneho', 'kraja', 'samospravny', 'fondy', 'europske', 'pravnickej', 'zastupenie', 'zahranicnej', 'zboru', 'zeleznic', 'ozbrojenej', 'ochrany', 'polnohospodarsky', 'politickej', 'politickeho', 'hnutia', 'zdravotne', 'socialna', 'poistovne', 'sucasne', 'or', 'ako', 'zapisv', 'samhosprolnik', 'podnikatel', 'podnikajuca', 'slobodne', 'zaklade', 'povolanie', 'ineho', 'zivnostenskeho', 'polnohospodarske', 'neinvesticny', 'zeleznicno', 'inspekcie', 'technickej', 'statnej', 'oblastny', 'statna', 'uradom', 'riadena', 'okresnym', 'jednoducha', 'zakladna', 'zdruzenia', 'medzinarodne', 'bydliskom', 'poistovaci', 'spolok', 'spolocna', 'druzstiev', 'zaujmova', 'cinna', 'danoveho', 'prilezitostne', 'informacneho', 'zapisana', 'skoly', 'pracovisko', 'vysokej', 'fakulty', 'ine', 'zahranicno', 'poistovna', 'cirkevna', 'penazny', 'doplnkova', 'dochodkova', 'vyrobne', 'zlozka', 'podniku', 'zariadenie', 'alebo', 'komanditna', 'zdruzenie', 'medzinarodneho', 'komor', 'vynimkou', 'profesnych', 'fakulta', 'mesto', 'zapisujuca', 'ina', 'obchodneho', 'registra', 'sa', 'pravnou', 'odvodenou', 'prispevkovej', 'subjektivitou', 'statneho', 'ustavu', 'penazneho', 'zakladatelmi', 'spolocny', 'viacerymi', 'sporitelna', 'neurcene', 'zatial', 'nespecifikovana', 'forma', 'pravna', 'spotrebne', 'prevadzkaren', 'obecneho', 'ai', 'zvaz', 'klub', 'sposobilosti', 'miestna', 'bez', 'pravnej', 'zaujmove', 'nezapisv', 'povolanim', 'slobodnym', 'slovenska', 'narodna', 'svojpomocne', 'spravy', 'verejnej', 'zeleznice', 'nadacia', 'oblastna', 'uzemnej', 'spoluprace', 'zoskupenie', 'poskytujuca', 'vseobecne', 'prospesne', 'neziskova', 'sluzby', 'televizna', 'kulturne', 'stredisko', 'tlacova', 'rozhlasova', 'informacne', 'obmedzenym', 'hnutie', 'zahranicneho', 'zahranicnou', 'ucastou', 'verejnopravna', 'institucia', 'hospodarskych', 'zaujmov', 'fyzickych', 'pozemkov', 'vlastnikov', 'pod', 'spolocenstva', 'bytov', 'delniska', 'druzba', 'omejeno', 'odgovornostjo', 'neomejeno', 'secondary', 'primary', 'state', 'owned', 'personal', 'tertiary', 'sociedad', 'laboral', 'o', 'responsabilidad', 'empresario', 'profesional', 'colectiva', 'regular', 'ahorros', 'caja', 'inmobiliaria', 'inversion', 'sociedades', 'nueva', 'mutualidad', 'prevision', 'civil', 'riesgo', 'agrupacion', 'pyme', 'responsablidad', 'del', 'mercado', 'activos', 'monetario', 'fondo', 'pensiones', 'comanditaria', 'acciones', 'garantia', 'reciproca', 'emprendedor', 'institucion', 'fondos', 'credito', 'mobiliaria', 'naringsverksamhet', 'som', 'ideell', 'bedriver', 'trossamfund', 'medlemsbank', 'europabolag', 'europakooperativ', 'sambruksforening', 'handelsbolag', 'bankaktiebolag', 'ekonomisk', 'kommanditbolag', 'sparbank', 'forsakringsforening', 'omsesidigt', 'forsakringsbolag', 'forsakringsaktiebolag', 'kooperativ', 'hyresrattsforening', 'intressegruppering', 'territoriellt', 'samarbete', 'gruppering', 'bostadsrattsforening', 'bostadsforening', 'aktiebolag', 'niederlassung', 'nicht', 'im', 'eingetragen', 'handelsregister', 'verwaltung', 'auslandisches', 'offentliches', 'bundes', 'gmbh', 'sicaf', 'investmentgesellschaft', 'festem', 'kapital', 'besondere', 'offentlichen', 'institut', 'einzelunternehmen', 'korperschaft', 'kantons', 'gemeinde', 'prokuren', 'nichtkaufmannische', 'von', 'gemeinderschaften', 'haupt', 'kollektive', 'kapitalanlagen', 'fuer', 'schweizerische', 'zweigniederlassung', 'bezirks', 'kommanditaktiengesellschaft', 'variablem', 'domiciled', 'enterprise', 'register', 'swiss', 'abroad', 'embassy', 'eg', 'federal', 'fixed', 'form', 'sector', 'cantonal', 'registrer', 'power', 'attorney', 'corpororate', 'undivided', 'representative', 'ownership', 'investments', 'registry', 'at', 'patnership', 'domiciliee', 'suisse', 'succursale', 'ex', 'ambassade', 'confederation', 'particuliere', 'canton', 'communale', 'religieuse', 'politique', 'etc', 'cantonale', 'procurations', 'commerciales', 'corpororation', 'representants', 'indivisions', 'collectifs', 'placements', 'enregistree', 'succursali', 'estero', 'iscritta', 'registro', 'domiciliata', 'commercio', 'una', 'all', 'svizzere', 'ambasciata', 'pubblica', 'amministrazione', 'estera', 'confederazione', 'della', 'sagl', 'garanzia', 'fisso', 'investimento', 'capitale', 'natura', 'particolare', 'istituti', 'ditta', 'accomandita', 'internazionali', 'organizazioni', 'patriziati', 'consorzi', 'amm', 'corporazioni', 'cantone', 'comunale', 'associazione', 'ecc', 'scientifico', 'religioso', 'politico', 'procura', 'corporazione', 'indivisioni', 'rappresentanti', 'd', 'straniera', 'collettivi', 'investimenti', 'svizzera', 'registrata', 'nel', 'distretto', 'variabile', 'kollektif', 'sirket', 'komandit', 'anonim', 'cyhoeddus', 'cyfyngedig', 'cwmni', 'partneriaeth', 'atebolrwydd', 'establishment', 'unregistered', 'old', 'nonprofit', 'development', 'benefit', 'membership', 'electric', 'marketing', 'transmission', 'firms', 'trusts', 'financial', 'partership', 'producer', 'cemetery', 'investor', 'county', 'railroad', 'savings', 'communit', 'l3c', 'transportation', 'authority', 'captive', 'bank', 'burial', 'statutory', 'series', 'llc', 'ednolichen', 'targovets', 'kooperatsia', 'ednolichno', 'aktsionerno', 'druzhestvo', 'sd', 'sadruzhie', 'sabiratelno', 's', 'komanditno', 'aktsii', 'sas', 'tsel', 'investitsionna', 'spetsialna', 'evropeysko', 'za', 'po', 'dogovorite', 'uchredeno', 'zadalzheniyata', 'i', 'zakona', 'kooperativno', 'ogranichena', 'otgovornost', 'union', 'odgovornoscu', 'drustvo', 'ogranicenom', 'morfi', 'nomiki', 'alli', 'synetairismos', 'etaireia', 'periorismenis', 'evropaiki', 'dimosia', 'efthynis', 'metoches', 'me', 'eponymia', 'emporiki', 'idrymata', 'kai', 'somateia', 'allodapi', 'ergazomenos', 'aftotelos', 'engyisi', 'echei', 'pou', 'metochiko', 'kefalaio', 'idiotiki', 'pronoias', 'tameia', 'syntaxeos', 'diepontai', 'ontotites', 'dimosio', 'apo', 'dikaio', 'to', 'synergatika', 'pistotika', 'choris', 'naftiki', 'eteria', 'eterorithmi', 'euthinis', 'astiki', 'proswpiki', 'sinetairismos', 'lipa', 'prosopa', 'dikeou', 'dimosiou', 'nomika', 'afanis', 'kinopraxia', 'kefaleouhiki', 'somatia', 'idrimata', 'omorithmi', 'kata', 'eterorrythmi', 'simplioktisia', 'anonimi', 'gu', 'si', 'fen', 'gong', 'xian', 'ren', 'you', 'ce', 'tuo', 'zhu', 'shou', 'fa', 'yan', 'cheng', 'li', 'ju', 'shi', 'de', 'gen', 'zhong', 'gang', 'fei', 'xiang', 'ben', 'wu', 'dan', 'bao', 'ze', 'huo', 'he', 'altro', 'a', 'stato', 'leggi', 'base', 'di', 'societa', 'in', 'costituita', 'semplice', 'responsabilita', 'semplificata', 'limitata', 'cooperativa', 'europea', 'consortile', 'azioni', 'per', 'collettivo', 'nome', 'soccorso', 'mutuo', 'professionisti', 'tra', 'societe', 'europeenne', 'companies', 'limited', 'by', 'private', 'guarantee', 'public', 'akcii', 'so', 'akcionersko', 'javno', 'trgovsko', 'pretprijatie', 'zaednica', 'interesna', 'stopanska', 'ogranicena', 'odgvornost', 'na', 'odnosno', 'trgovec', 'poedinec', 'stransko', 'stranski', 'podruznica', 'assotsiatsii', 'organizatsiy', 'blagotvoritel', 'nykh', 'obyedineniya', 'soyuzy', 'otvetstvennost', 'ogranichennoy', 'yu', 'obshchestva', 'khozyaystva', 'yanskiye', 'krest', 'fermerskiye', 'nekommercheskiye', 'organizatsii', 'avtonomnyye', 'nyye', 'uchrezhdeniya', 'obyedineniy', 'obshchestvennykh', 'kooperativov', 'munitsipal', 'tovarishchestva', 'sobstvennikov', 'zhil', 'ya', 'federal', 'kazennyye', 'predpriyatiya', 'sel', 'kooperativy', 'skokhozyaystvennyye', 'proizvodstvennyye', 'skokhozyaystvennykh', 'proizvodstvennykh', 'krome', 'profsoyuznyye', 'prochiye', 'kommercheskimi', 'yuridicheskiye', 'yavlyayushchiyesya', 'litsa', 'organizatsiyami', 'sozdannyye', 'subyektom', 'federatsii', 'rossiyskoy', 'publichnyye', 'aktsionernyye', 'advokatskiy', 'advokaty', 'kabinet', 'uchredivshiye', 'zhivotnovodcheskiye', 'skiye', 'potrebitel', 'ili', 'zhilishchnyye', 'zhilishchno', 'stroitel', 'nauk', 'akademii', 'gosudarstvennyye', 'byudzhetnyye', 'subyektov', 'ogorodnicheskiye', 'sadovodcheskiye', 'dachnyye', 'kompanii', 'publichno', 'pravovyye', 'sovety', 'obrazovaniy', 'unitarnyye', 'byuro', 'advokatskiye', 'vnesennyye', 'reyestr', 'v', 'kazach', 'ikh', 'gosudarstvennyy', 'obshchestv', 'kreditnyye', 'garazhno', 'garazhnyye', 'grazhdan', 'dlya', 'lits', 'nosti', 'fizicheskikh', 'formy', 'deyatel', 'organizatsionno', 'pravovyyу', 'yuridicheskikh', 'yavlyayushchikhsya', 'korporativnymi', 'dachnykh', 'ogorodnicheskikh', 'nekommercheskikh', 'sadovodcheskikh', 'partnerstva', 'fondy', 'prokata', 'ekologicheskiye', 'obshchestvennyye', 'korporatsii', 'kommercheskoy', 'arteli', 'territorial', 'samoupravleniya', 'federatsiyey', 'malochislennykh', 'narodov', 'obshchiny', 'korennykh', 'podrazdeleniy', 'obosoblennykh', 'strukturnyye', 'podrazdeleniya', 'nedvizhimosti', 'urovnya', 'vtorogo', 'palaty', 'religioznyye', 'obsluzhivayushchiye', 'pererabatyvayushchiye', 'nekommercheskimi', 'unitarnymi', 'snabzhencheskiye', 'kolkhozy', 'samoreguliruyemyye', 'kommanditnyye', 'vere', 'prostyye', 'prav', 'sozdannykh', 'bez', 'yuridicheskogo', 'nepublichnyye', 'khozyaystvennyye', 'khozyaystv', 'yanskikh', 'fermerskikh', 'glavy', 'obshchestvennoy', 'samodeyatel', 'organy', 'inostrannykh', 'stvennykh', 'otdeleniya', 'nepravitel', 'partii', 'politicheskiye', 'sbytovyye', 'torgovyye', 'predstavitel', 'stva', 'upravleniya', 'prave', 'operativnogo', 'osnovannyye', 'predprinimateli', 'individual', 'ekonomicheskogo', 'vzaimodeystviya', 'notarial', 'mezhpravitel', 'mezhdunarodnyye', 'stvennyye', 'obrazovaniyem', 'nym', 'vzaimnogo', 'strakhovaniya', 'territorii', 'mezhdunarodnykh', 'osushchestvlyayushchikh', 'nost', 'zanimayushchiyesya', 'praktikoy', 'notariusy', 'chastnoy', 'khozyaystvennogo', 'vedeniya', 'rabotodateley', 'ne', 'predprinimatel', 'otnesennoy', 'k', 'stvu', 'skikh', 'kollegii', 'advokatov', 'gorodskiye', 'rayonnyye', 'mezhrayonnyye', 'sudy', 'rybolovetskiye', 'obosoblennyye', 'filialy', 'nakopitel', 'kreditnykh', 'koopkhozy', 'kooperativnyye', 'obshchin', 'chastnyye', 'investitsionnyye', 'payevyye', 'dvizheniya', 'negosudarstvennyye', 'pensionnyye', 'promyshlennyye', 'torgovo', 'polnyye', 'zadruzni', 'savez', 'preduzece', 'drustveno', 'preduzetnik', 'zadruga', 'sa', 'akcionarsko', 'ortacko', 'business', 'international', 'corporation', 'sce', 'keg', 'gesmbh', 'gmbh', 'eu', 'ag', 'ohg', 'og', 'oeg', 'se', 'kg', 'rechtstrager', 'sonstiger', 'privatstiftung', 'genossenschaft', 'europaische', 'sce', 'kommandit', 'erwerbsgesellschaft', 'mit', 'haftung', 'gesellschaft', 'beschrankter', 'auf', 'versicherungsverein', 'gegenseitigkeit', 'interessenvereinigung', 'wirtschaftliche', 'einzelunternehmer', 'aktiengesellschaft', 'einzelkaufmann', 'offene', 'handelsgesellschaft', 'sparkasse', 'erwerbs', 'und', 'wirtschaftsgenossenschaft', 'se', 'kommanditgesellschaft', 'operative', 'limited', 'cooperative', 'coop', 'op', 'co', 'ltd', 'inc', 'lp', 'ilp', 'no', 'liability', 'nl', 'proprietary', 'pty', 'corporation', 'indigenous', 'rntbc', 'corporation', 'operative', 'co', 'association', 'incorporated', 'partnership', 'limited', 'by', 'public', 'company', 'guarantee', 'no', 'liability', 'proprietary', 'unlimited', 'shares', 'indigenous', 'vof', 'bv', 'nv', 'avv', 'vba', 'stichting', 'vennootschap', 'onder', 'firma', 'commanditaire', '1', 'besloten', 'vereniging', 'naamloze', 'cooperatieve', 'eenmanszaak', 'vrijgestelde', 'aruba', 'recht', 'buitenlands', 'maatschap', 'beperkte', 'met', 'aansprakelijkheid', '1+', 'vof', 'bv', 'nv', 'sce', 'ag', 'ohg', 'se', 'kgaamsz', 'gbhsz', 'ages', 'unp', 'guhsz', 'ewiv', 'genmbh', 'eog', 'ohgmsz', 'pgmbhma', 'gvorp', 'orvohgza', 'gmuhgb', 'wiv', 'pmbhsz', 'kgaa', 'zrg', 'gar', 'genmubh', 'ekg', 'pgmbh', 'wivmsz', 'zvggbh', 'pgbhsz', 'oe', 'o', 'rag', 'lg', 'ivog', 'zvgpgbh', 'vog', 'zvggugch', 'ofrgmbh', 'ekgmsz', 'prst', 'ofp', 'agmsz', 'gns', 'fs', 'sca', 'scrl', 'ent', 'e', 'epp', 'scri', 'geie', 'isbl', 'snc', 'sprlu', 'saspj', 'dpu', 'asbl', 'cp', 'gie', 'sprl', 'sc', 'sdc', 'scs', 'etspubli', 'sa', 'sagr', 'aisbl', 'fondpriv', 's', 'agr', 'fup', 'so', 'cva', 'cvba', 'bo', 'onp', 'cvoa', 'eesv', 'izw', 'ebvba', 'vvzrl', 'pr', 'vzw', 'cd', 'group', 'esv', 'bvba', 'ms', 'commv', 'oi', 'gcv', 'commva', 'lv', 'ivzw', 'gcw', 'priv', 'st', 'son', 'stichting', 'vennootschap', 'onder', 'firma', 'commanditaire', 'besloten', 'vereniging', 'naamloze', 'cooperatieve', 'recht', 'maatschap', 'beperkte', 'met', 'aansprakelijkheid', 'association', 'public', 'privatstiftung', 'genossenschaft', 'europaische', 'mit', 'haftung', 'gesellschaft', 'beschrankter', 'auf', 'interessenvereinigung', 'wirtschaftliche', 'aktiengesellschaft', 'offene', 'handelsgesellschaft', 'kommanditgesellschaft', 'sozialer', 'zielsetzung', 'aktien', 'europaea', 'societas', 'auslandische', 'naturliche', 'person', 'unternehmen', 'unbeschrankter', 'einrichtung', 'gewinnerzielungsabsicht', 'ohne', 'alleingesellschafter', 'privatgesellschaft', 'einem', 'oder', 'rechtspersonlichkeit', 'gesellschaften', 'vereinigungen', 'rechtliche', 'offentlich', 'vereinigung', 'beteiligung', 'rechtsform', 'zivilrechtliche', 'einer', 'in', 'der', 'rechts', 'allgemeinen', 'des', 'einfache', 'offentliche', 'einfachen', 'offenen', 'landwirtschaftlichen', 'internationale', 'landwirtschaftliche', 'gemeinnutzige', 'stiftung', 'commandite', 'finalite', 'sociale', 'actions', 'societe', 'cooperative', 'responsabilite', 'limitee', 'europeenne', 'entreprise', 'etrangere', 'physique', 'personne', 'illimitee', 'economique', 'groupement', 'europeen', 'interet', 'lucratif', 'but', 'sans', 'institution', 'nom', 'collectif', 'unipersonnelle', 'privee', 'personnalite', 'juridique', 'droit', 'participation', 'civile', 'sous', 'forme', 'commun', 'simple', 'etablissement', 'anonyme', 'agricole', 'fondation', 'publique', 'utilite', 'oogmerk', 'op', 'sociaal', 'aandelen', 'een', 'europese', 'buitenlandse', 'onderneming', 'persoon', 'natuurlijk', 'onbeperkte', 'europees', 'economisch', 'samenwerkingsverband', 'instelling', 'winstoogmerk', 'zonder', 'eenpersoons', 'of', 'rechtspersoonlijkheid', 'publiek', 'van', 'wijze', 'bij', 'deelneming', 'burgerlijke', 'vorm', 'gewone', 'openbare', 'landbouwvennootschap', 'bv', 'lv', 'private', 'nut', 'openbaar', 'ет', 'еад', 'с', 'ие', 'кда', 'адсиц', 'кд', 'ед', 'дззд', 'екд', 'оод', 'ад', 'еоод', 'et', 'coop', 'ead', 'ie', 's', 'sd', 'kda', 'adsic', 'kd', 'dzzd', 'ood', 'ad', 'eood', 'едноличен', 'търговец', 'кооперация', 'акционерно', 'дружество', 'еднолично', 'съдружие', 'събирателно', 'сд', 'командиртно', 'акции', 'с', 'инвестиционна', 'със', 'специална', 'цел', 'европеиско', 'задълженията', 'договорите', 'за', 'закона', 'и', 'учредено', 'по', 'кооперативно', 'отговорност', 'ограничена', 'ednolichen', 'targovets', 'kooperatsia', 'ednolichno', 'aktsionerno', 'druzhestvo', 'sd', 'sadruzhie', 'sabiratelno', 's', 'komanditno', 'aktsii', 'sas', 'tsel', 'investitsionna', 'spetsialna', 'evropeysko', 'za', 'po', 'dogovorite', 'uchredeno', 'zadalzheniyata', 'i', 'zakona', 'kooperativno', 'ogranichena', 'otgovornost', 'stichting', 'vennootschap', 'onder', 'firma', 'commanditaire', 'besloten', 'vereniging', 'naamloze', 'eenmanszaak', 'recht', 'maatschap', 'beperkte', 'met', 'op', 'group', 'aandelen', 'een', 'buitenlandse', 'zonder', 'nederlands', 'naar', 'meerdere', 'vennoten', 'beherende', 'rechtsbevoegdheid', 'aandeelhouder', 'bestuurde', 'particulier', 'fonds', 'hoofdvestiging', 'buiten', 'bonaire', 'nevenvestiging', 'volledige', 'eigenaren', 'rechtsvorm', 'cooperatie', 'beherend', 'vennoot', 'limited', 'by', 'public', 'guarantee', 'liability', 'private', 'group', 'close', 'companies', 'operative', 'limited', 'cooperative', 'coop', 'groupe', 'op', 'co', 'ltd', 'inc', 'lp', 'no', 'liability', 'group', 'corporation', 'cp', 'sa', 'srl', 'llp', 'sencrl', 'corp', 'pc', 'company', 'loan', 'trustco', 'trustee', 'trust', 'ltee', 'limitee', 'union', 'condominium', 'partnership', 'incorporated', 'by', 'guarantee', 'society', 'association', 'communautaire', 'cic', 'sic', 'interest', 'interet', 'community', 'societe', 'd', 'ulc', 'trustees', 'fiduciaires', 'manitoba', 'incorporee', 'a', 'responabilite', 'pool', 'parish', 'catholic', 'paroisse', 'catholique', 'ukrainienne', 'ukrainian', 'commandite', 'en', 'sarf', 'pret', 'compagnie', 'de', 'fiduciaire', 'fiducie', 'cer', 'cooperation', 'cooperatif', 'sec', 'senc', 'coop', 'cooperation', 'cooperative', 'corp', 'ltd', 'inc', 'business', 'corporation', 'operative', 'co', 'association', 'incorporated', 'partnership', 'limited', 'by', 'public', 'company', 'guarantee', 'liability', 'unlimited', 'shares', 'in', 'commandite', 'actions', 'societe', 'cooperative', 'responsabilite', 'limitee', 'entreprise', 'etrangere', 'personne', 'economique', 'lucratif', 'but', 'sans', 'nom', 'collectif', 'participation', 'agricole', 'publique', 'private', 'fonds', 'trade', 'name', 'sole', 'proprietorship', 'trust', 'alberta', 'utility', 'rural', 'professional', 'loan', 'union', 'society', 'general', 'act', 'non', 'profit', 'corp', 'agricultural', 'religious', 'service', 'includes', 'housing', 'community', 'outside', 'bc', 'formed', 'fund', 'pension', 'fire', 'mutual', 'insurance', 'extraprovincial', 'share', 'registered', 'foreign', 'entity', 'funded', 'member', 'contribution', 'board', 'parliament', 'corporations', 'enacted', 'capital', 'without', 'fair', 'condominium', 'project', 'new', 'brunswick', 'proprietor', 'depends', 'on', 'legislature', 'unions', 'condominiums', 'not', 'operatives', 'for', 'ns', 'partnerships', 'holding', 'investment', 'interest', 'names', 'proprietors', 'ontario', 'legislative', 'assembly', 'v', 'part', 'under', 'which', 'liabilty', 'saskatchewan', 'generation', 'syndicates', 'ventures', 'joint', 'recreation', 'including', 'lawyers', 'accountants', 'extra', 'provincial', 'only', 'manitoba', 'parish', 'catholic', 'ukrainian', 'registration', 'territorial', 'nt', 'authorized', 'commerce', 'chambre', 'parlement', 'constituee', 'loi', 'organisation', 'retraite', 'professionnelle', 'compagnie', 'pret', 'nouveau', 'selon', 'condominiale', 'fiducie', 'gerant', 'projet', 'morale', 'residante', 'agricoles', 'foires', 'unique', 'appellation', 'commerciale', 'proprietaire', 'cooperatif', 'syndicat', 'quebec', 'caractere', 'speciale', 'trois', 'colomb', 'federation', 'colleges', 'services', 'concernant', 'etablissements', 'conservation', 'cruaute', 'commissions', 'partie', 'sociaux', 'jean', 'peche', 'marche', 'certaines', 'territoires', 'cimetieres', 'produits', 'clubs', 'eveques', 'faune', 'iii', 'detention', 'decrets', 'professionnels', 'cris', 'animaux', 'habitation', 'cooperatives', 'regionale', 'fabriques', 'saint', 'cimetiere', 'catholiques', 'urbanisme', 'chasse', 'administration', 'scolaires', 'autochtones', 'guides', 'bienfaisance', 'territoriale', 'laitieres', 'securite', 'associations', 'baptiste', 'certains', 'chevaliers', 'agriculture', 'professionnelles', 'œuvre', 'instruction', 'enseignement', 'compagnies', 'travail', 'nordiques', 'sante', 'cercles', 'rivieres', 'syndicats', 'province', 'religieuses', 'municipale', 'envers', 'constitution', 'probation', 'nationales', 'mise', 'code', 'qualification', 'horticulture', 'romains', 'valeur', 'amenagement', 'formation', 'minieres', 'kativik', 'scouts', 'main', 'villages', 'ii', 'eglises', 'alimentaires', 'collective', 'pour', 'assurances', 'preventives', 'professions', 'correctionnels', 'regroupement', 'miniers', 'villes', 'gestion', 'societes', 'professionnel', 'convention', 'cites', 'epargne', 'eau', 'patrons', 'mutuel', 'constitue', 'flottage', 'quebecoise', 'acte', 'developpement', 'entraide', 'miniere', 'gaz', 'electricite', 'laitiers', 'elevage', 'fideicommis', 'producteurs', 'telephone', 'exploration', 'construction', 'telegraphe', 'copropriete', 'prive', 'union', 'coop', 'co', 'ltd', 'corporation', 'gmbh', 'ag', 'ent', 'sa', 'corp', 'partnership', 'commandite', 'en', 'sec', 'plc', 'rc', 'per', 'sarl', 'org', 'soc', 'com', 'gen', 'ausl', 'botschaft', 'gesellsch', 'einfache', 'rechtsform', 'bund', 'inst', 'recht', 'off', 'einzelfirma', 'unt', 'kommanditgesellsch', 'organisation', 'int', 'rechtl', 'korp', 'kanton', 'gemeinde', 'prokura', 'kollektivgesellsch', 'aus', 'kommandit', 'kapitalanlagen', 'hr', 'zweig', 'bezirk', 'foreign', 'ltdco', 'embassy', 'simple', 'legal', 'nature', 'federal', 'administration', 'pub', 'individually', 'owned', 'fed', 'publ', 'internat', 'public', 'cantonal', 'local', 'cant', 'att', 'power', 'loc', 'general', 'undivided', 'enterprise', 'part', 'coll', 'invest', 'group', 'branch', 'distr', 'district', 'etranger', 'ambassade', 'etran', 'jur', 'confederation', 'droit', 'raison', 'individuelle', 'federale', 'internationales', 'canton', 'commune', 'cantonale', 'sadom', 'procuration', 'communale', 'corpor', 'collectif', 'nom', 'indivisions', 'etrangere', 'investissement', 'succ', 'action', 'comm', 'estero', 'sagl', 'ambasciate', 'estera', 'natura', 'guiri', 'confederazione', 'pubblico', 'dir', 'ist', 'individuale', 'ragione', 'imp', 'pubb', 'accomandita', 'in', 'internazionali', 'diritto', 'cantone', 'comune', 'dom', 'procura', 'comunale', 'corpora', 'collettivo', 'nome', 'indivisioni', 'str', 'investimenti', 'distretto', 'azioni', 'international', 'corporation', 'association', 'partnership', 'limited', 'by', 'public', 'company', 'liability', 'shares', 'genossenschaft', 'mit', 'haftung', 'gesellschaft', 'beschrankter', 'aktiengesellschaft', 'kommanditgesellschaft', 'auslandische', 'unternehmen', 'rechtliche', 'offentlich', 'rechtsform', 'in', 'der', 'rechts', 'des', 'einfache', 'offentliche', 'internationale', 'stiftung', 'commandite', 'societe', 'cooperative', 'responsabilite', 'limitee', 'entreprise', 'etrangere', 'institution', 'nom', 'collectif', 'juridique', 'droit', 'forme', 'simple', 'anonyme', 'fondation', 'publique', 'sole', 'proprietorship', 'general', 'non', 'registered', 'foreign', 'capital', 'not', 'for', 'investment', 'commerce', 'organisation', 'commerciale', 'administration', 'collective', 'cooperativa', 'a', 'sarl', 'etranger', 'action', 'registre', 'inscrite', 'local', 'district', 'investissement', 'federale', 'commercial', 'scientifique', 'special', 'sicav', 'variable', 'individuelle', 'verein', 'foundation', 'with', 'legal', 'di', 'societa', 'ente', 'semplice', 'pubblico', 'diritto', 'impresa', 'fondazione', 'limitata', 'giuridica', 'al', 'individuale', 'azioni', 'per', 'nome', 'collettivo', 'kollektivgesellschaft', 'fixe', 'anonima', 'branch', 'o', 'del', 'niederlassung', 'nicht', 'im', 'eingetragen', 'handelsregister', 'verwaltung', 'auslandisches', 'offentliches', 'bundes', 'gmbh', 'sicaf', 'investmentgesellschaft', 'festem', 'kapital', 'besondere', 'offentlichen', 'institut', 'einzelunternehmen', 'korperschaft', 'kantons', 'gemeinde', 'prokuren', 'nichtkaufmannische', 'von', 'gemeinderschaften', 'haupt', 'kollektive', 'kapitalanlagen', 'fuer', 'schweizerische', 'zweigniederlassung', 'bezirks', 'kommanditaktiengesellschaft', 'variablem', 'domiciled', 'enterprise', 'register', 'swiss', 'abroad', 'embassy', 'eg', 'federal', 'fixed', 'form', 'sector', 'cantonal', 'registrer', 'power', 'attorney', 'corpororate', 'undivided', 'representative', 'ownership', 'investments', 'registry', 'at', 'patnership', 'domiciliee', 'suisse', 'succursale', 'ex', 'ambassade', 'confederation', 'particuliere', 'canton', 'communale', 'religieuse', 'politique', 'etc', 'cantonale', 'procurations', 'commerciales', 'corpororation', 'representants', 'indivisions', 'collectifs', 'placements', 'enregistree', 'succursali', 'estero', 'iscritta', 'registro', 'domiciliata', 'commercio', 'una', 'all', 'svizzere', 'ambasciata', 'pubblica', 'amministrazione', 'estera', 'confederazione', 'della', 'sagl', 'garanzia', 'fisso', 'investimento', 'capitale', 'natura', 'particolare', 'istituti', 'ditta', 'accomandita', 'internazionali', 'organizazioni', 'patriziati', 'consorzi', 'amm', 'corporazioni', 'cantone', 'comunale', 'associazione', 'ecc', 'scientifico', 'religioso', 'politico', 'procura', 'corporazione', 'indivisioni', 'rappresentanti', 'd', 'straniera', 'collettivi', 'investimenti', 'svizzera', 'registrata', 'nel', 'distretto', 'variabile', 'stichting', 'vennootschap', 'commanditaire', 'besloten', 'vereniging', 'naamloze', 'eenmanszaak', 'openbare', 'particulier', 'fonds', 'cooperatie', 'trust', 'stille', 'rederij', 'onderlinge', 'waarborgmaatschappij', 'νομικη', 'μορφη', 'αλλη', 'συνεταιρισμοσ', 'δημοσια', 'ευθυνησ', 'ευρωπαικη', 'εταιρεια', 'περιορισμενησ', 'με', 'μετοχεσ', 'επωνυμια', 'eμπορικη', 'σωματεια', 'ιδρυματα', 'και', 'αλλοδαπη', 'αυτοτελωσ', 'εργαζομενοσ', 'εχει', 'κεφαλαιο', 'μετοχικο', 'εγγυηση', 'που', 'ιδιωτικη', 'group', 'προνοιασ', 'συνταξεωσ', 'ταμεια', 'οντοτητεσ', 'διεπονται', 'δημοσιο', 'απο', 'δικαιο', 'το', 'πιστωτικα', 'συνεργατικα', 'χωρισ', 'morfi', 'nomiki', 'alli', 'synetairismos', 'etaireia', 'periorismenis', 'evropaiki', 'dimosia', 'efthynis', 'metoches', 'me', 'eponymia', 'emporiki', 'idrymata', 'kai', 'somateia', 'allodapi', 'ergazomenos', 'aftotelos', 'engyisi', 'echei', 'pou', 'metochiko', 'kefalaio', 'idiotiki', 'pronoias', 'tameia', 'syntaxeos', 'diepontai', 'ontotites', 'dimosio', 'apo', 'dikaio', 'to', 'synergatika', 'pistotika', 'choris', '1', 'se', 'v', 's', 'svepomocne', 'zemedelske', 'druzstvo', 'zarizeni', 'strany', 'nebo', 'podnik', 'hospodarske', 'politicke', 'konsolidacni', 'ceska', 'agentura', 'evropske', 'pro', 'spolupraci', 'seskupeni', 'uzemni', 'nadace', 'fond', 'zakona', 'group', 'ze', 'statni', 'zajmova', 'druzstev', 'organizace', 'regionalni', 'rada', 'soudrznosti', 'regionu', 'cennymi', 'papiry', 'obchodniku', 'garancni', 'staly', 'rozhodci', 'soud', 'zamestnavatelu', 'pobocna', 'mezinarodni', 'verejna', 'obchodni', 'spolecnost', 'akciova', 'sdruzeni', 'organizacni', 'jednotka', 'obcanskeho', 'na', 'komanditni', 'akcie', 'ostatni', 'prispevkova', 'zajmove', 'hospodarska', 'uradem', 'rizena', 'okresnim', 'spotrebni', 'tiskova', 'kancelar', 'tuzemska', 'fyzicka', 'osoba', 'podnikajici', 'rucenim', 'omezenym', 'obcanske', 'do', 'nezapisujici', 'rejstriku', 'obchodniho', 'zeleznicni', 'cesty', 'sprava', 'dopravni', 'prospesna', 'obecne', 'zdravotni', 'vseobecna', 'pojistovna', 'drobna', 'uradu', 'obecniho', 'provozovna', 'samostatna', 'vyrobni', 'spolek', 'ucasti', 'majetkovou', 'zahranicni', 'instituce', 'vyzkumna', 'skolska', 'pravnicka', 'cirkvi', 'spolecnosti', 'a', 'svazy', 'nabozenskych', 'ustav', 'penezni', 'banka', 'cirkve', 'nabozenske', 'pobocny', 'neziskove', 'verejne', 'ustavni', 'zdravotnicke', 'agrarni', 'komora', 'statu', 'slozky', 'vnitrni', 'obchodu', 'zahranicniho', 'slozka', 'nadacniho', 'fondu', 'mezinarodniho', 'zvlastni', 'organizacich', 'mezinarodnich', 'zastoupeni', 'zajmu', 'nevladnich', 'ceskych', 'jednotek', 'spolecenstvi', 'vlastniku', 'obec', 'evidovane', 'osoby', 'pravnicke', 'cirkevni', 'ceskoslovenska', 'honebni', 'spolecenstvo', 'ceskoslovenske', 'drahy', 'odborova', 'obci', 'dobrovolny', 'svazek', 'samospravnym', 'uzemnim', 'zrizena', 'celkem', 'verejnopravni', 'vice', 'zakladateli', 'spolecny', 'narodni', 'komoditni', 'burza', 'samospravna', 'stavovska', 'profesni', 'vysoka', 'skola', 'mestska', 'cast', 'obvod', 'mestsky', 'nevladni', 'kraj', 'verejny', 'auditem', 'nad', 'dohled', 'mimo', 'vzp', 'nadacni', 'zakladatelem', 'druzstevni', 'obecni', 'evropska', 'bytove', 'odstepny', 'zavod', 'fyzicke', 'spolecna', 'osob', 'pravnickych', 'zemedelsky', 'ucelova', 'zahranicne', 'verejneho', 'zakonem', 'pravnikca', 'zapisovana', 'zvlastnim', 'strana', 'politicka', 'hnuti', 'jine', 'sce', 'gmbh', 'ag', 'ohg', 'se', 'kg', 'ewiv', 'kgaa', 'e', 'k', 'vvag', 'mbb', 'partg', 'ug', 'ek', 'ev', 'eg', 'genossenschaft', 'europaische', 'mit', 'haftung', 'gesellschaft', 'beschrankter', 'auf', 'versicherungsverein', 'gegenseitigkeit', 'interessenvereinigung', 'wirtschaftliche', 'aktiengesellschaft', 'offene', 'handelsgesellschaft', 'kommanditgesellschaft', 'aktien', 'berufshaftung', 'partnerschaftsgesellschaft', 'unternehmergesellschaft', 'kaufmann', 'eingetragener', 'verein', 'sce', 'se', 's', 'a', 'ivs', 'i', 'p', 'selskab', 'smba', 'aps', 'k', 'amba', 'eøfg', 'fmba', 'iværksætterselskab', 'interessentskab', 'partnerselskab', 'enkeltmandsvirksomhed', 'andelsselskab', 'europæisk', 'begrænset', 'med', 'ansvar', 'selskab', 'anpartsselskab', 'medarbejderinvesteringsselskab', 'kommanditselskab', 'group', 'firmagruppe', 'økonomisk', 'forening', 'aktieselskab', 'sce', 'se', 'sa', 'fie', 'hu', 'ku', 'as', 'tu', 'au', 'ou', 'emhu', 'uu', 'mtu', 'tuh', 'sihtasutus', 'isikust', 'fuusilisest', 'ettevotja', 'hooneuhistu', 'ariuhing', 'euroopa', 'korteriuhistu', 'aktsiaselts', 'usuline', 'uhendus', 'erakond', 'taisuhing', 'ametiuhing', 'osauhing', 'majandushuviuhing', 'usaldusuhing', 'loomeliit', 'mittetulundusuhing', 'uhistu', 'tulundusuhistu', 'coop', 'se', 'e', 'cp', 'sc', 'sa', 's', 'srl', 'a', 'en', 'p', 'slp', 'fi', 'sl', 'srll', 'sll', 'scoop', 'scp', 'srcp', 'sii', 'slne', 'mps', 'sap', 'scr', 'scoopp', 'aeie', 'pyme', 'fiamm', 'group', 'fp', 'scom', 'scom:pap', 'aie', 'sgr', 'erl', 'srlp', 'fcr', 'iic', 'fii', 'sal', 'src', 'c', 'com', 'fim', 'scomp', 'simple', 'capital', 'cooperativa', 'social', 'economico', 'europea', 'mutua', 'en', 'de', 'anonima', 'empresa', 'por', 'limitada', 'individual', 'interes', 'sociedad', 'laboral', 'o', 'responsabilidad', 'empresario', 'profesional', 'colectiva', 'regular', 'ahorros', 'caja', 'inmobiliaria', 'inversion', 'sociedades', 'nueva', 'mutualidad', 'prevision', 'civil', 'riesgo', 'agrupacion', 'pyme', 'responsablidad', 'del', 'mercado', 'activos', 'monetario', 'fondo', 'pensiones', 'comanditaria', 'acciones', 'garantia', 'reciproca', 'emprendedor', 'institucion', 'fondos', 'credito', 'mobiliaria', 'association', 'public', 'internationale', 'test', 'commandite', 'sociale', 'actions', 'societe', 'cooperative', 'responsabilite', 'limitee', 'europeenne', 'entreprise', 'etrangere', 'physique', 'personne', 'economique', 'groupement', 'europeen', 'interet', 'sans', 'institution', 'nom', 'collectif', 'unipersonnelle', 'privee', 'personnalite', 'droit', 'participation', 'civile', 'forme', 'commun', 'simple', 'etablissement', 'anonyme', 'agricole', 'fondation', 'publique', 'utilite', 'rural', 'union', 'general', 'non', 'service', 'capital', 'territorial', 'commerce', 'organisation', 'retraite', 'professionnelle', 'fiducie', 'gerant', 'morale', 'group', 'agricoles', 'unique', 'commerciale', 'syndicat', 'caractere', 'habitation', 'cooperatives', 'regionale', 'administration', 'territoriale', 'securite', 'enseignement', 'amenagement', 'pour', 'professions', 'villes', 'gestion', 'societes', 'professionnel', 'epargne', 'mutuel', 'developpement', 'construction', 'copropriete', 'prive', 'collectivite', 'regie', 'locale', 'administratif', 'scp', 'medecins', 'salaries', 'autre', 'nationale', 'conseil', 'personnes', 'physiques', 'creee', 'entre', 'fait', 'sarl', 'attribution', 'entente', 'interregionale', 'etranger', 'etat', 'directoire', 'mutuelle', 'materiel', 'utilisation', 'cuma', 'simplifiee', 'exercice', 'liberal', 'action', 'registre', 'inscrite', 'notaires', 'incendie', 'secours', 'sdis', 'departemental', 'consommation', 'local', 'declaree', 'specialise', 'cooperation', 'autorisee', 'syndicale', 'hlm', 'liberale', 'profession', 'petr', 'equilibre', 'pole', 'foncier', 'prevoyance', 'commercant', 'social', 'medico', 'sai', 'supplementaire', 'sas', 'experts', 'geometres', 'financieres', 'spfpl', 'participations', 'maritime', 'geie', 'sica', 'veterinaires', 'forestier', 'groupe', 'dote', 'territoire', 'mer', 'outre', 'deconcentre', 'competence', 'inter', 'departementale', 'safer', 'juridiques', 'conseils', 'commune', 'deleguee', 'associee', 'regime', 'hors', 'defense', 'ministere', 'vente', 'immobiliere', 'assurance', 'mixte', 'economie', 'equipement', 'urbain', 'district', 'urbaine', 'fonciere', 'architectes', 'ouvriere', 'constitutionnelle', 'autorite', 'artisanale', 'exploitation', 'immobilier', 'infirmiers', 'investissement', 'paroisse', 'zone', 'concordataire', 'ensemble', 'mutualite', 'liberales', 'artisan', 'region', 'vocation', 'intercommunal', 'sivom', 'multiple', 'organisme', 'mutualiste', 'insertion', 'federale', 'production', 'secteur', 'industriel', 'centre', 'technique', 'comite', 'scop', 'national', 'commercial', 'comptable', 'appel', 'avoues', 'sicomi', 'industrie', 'immatricule', 'agence', 'rcs', 'representation', 'fonction', 'centrale', 'ayant', 'nouvelle', 'comptes', 'commissaires', 'smia', 'soins', 'ambulatoires', 'interprofessionnelles', 'assimile', 'ordre', 'commercants', 'detaillants', 'cias', 'greffiers', 'tribunal', 'transport', 'municipal', 'intermediaire', 'haut', 'bas', 'moselle', 'rhin', 'sivu', 'avocats', 'priseurs', 'laitiere', 'hospitalier', 'dentistes', 'communes', 'biens', 'commission', 'indivis', 'scientifique', 'culturel', 'propriete', 'progressive', 'accession', 'cercle', 'armees', 'dans', 'foyer', 'patronal', 'masseurs', 'kinesitherapeutes', 'special', 'associe', 'moyens', 'interdepartementale', 'alsace', 'agglomeration', 'communaute', 'pas', 'dependant', 'vieillesse', 'ne', 'ferme', 'banque', 'communal', 'remembrement', 'avec', 'indivision', 'congregation', 'metropole', 'immatriculee', 'gaec', 'consulaire', 'gie', 'sanitaire', 'sca', 'agent', 'chomage', 'ecoles', 'exploitant', 'ophlm', 'loyer', 'office', 'modere', 'caution', 'ecole', 'dotee', 'medicale', 'directeurs', 'laboratoire', 'analyse', 'central', 'hospitalisation', 'maladie', 'indication', 'sicav', 'variable', 'employeurs', 'huissiers', 'reconnue', 'section', 'departement', 'administrative', 'independante', 'metropolitain', 'officier', 'ministeriel', 'complementaire', 'scpi', 'placement', 'gip', 'pastoral', 'individuelle', 'ouvert', 'libre', 'lorraine', 'cultes', 'limited', 'ltd', 'lp', 'se', 'llp', 'eeig', 'plc', 'ccc', 'cyf', 'pac', 'br', 'partnership', 'limited', 'by', 'public', 'company', 'guarantee', 'liability', 'unlimited', 'group', 'europaea', 'societas', 'private', 'interest', 'economic', 'european', 'grouping', 'cyhoeddus', 'cyfyngedig', 'cwmni', 'partneriaeth', 'atebolrwydd', 'establishment', 'unregistered', 'old', 'ltd', 'lp', 'llp', 'fdn', 'partnership', 'limited', 'company', 'liability', 'foundation', 'partnertship', 'business', 'partnership', 'limited', 'by', 'public', 'company', 'guarantee', 'unlimited', 'private', 'name', 'sole', 'proprietorship', 'share', 'external', 'subsidiary', 'limited', 'ltd', 'lp', 'se', 'llp', 'eeig', 'ptc', 'plc', 'limited', 'by', 'public', 'company', 'guarantee', 'liability', 'unlimited', 'societe', 'private', 'trust', 'partnerships', 'interest', 'economic', 'european', 'groupings', 'foundations', 'europeas', 'coop', 'oe', 'sc', 'group', 'sa', 'ee', 'epe', 'sp', 'other', 'pl', 'slp', 'jv', 'ike', 'clf', 'jso', 'συνεταιρισμοσ', 'ευθυνησ', 'ευρωπαικη', 'εταιρεια', 'περιορισμενησ', 'μετοχεσ', 'σωματεια', 'ιδρυματα', 'ιδιωτικη', 'εταιρια', 'ναυτικη', 'ετερορρυθμη', 'αστικη', 'προσωπικη', 'λοιπα', 'δημοσιου', 'δικαιου', 'νομικα', 'προσωπα', 'αφανησ', 'κοινοπραξια', 'κεφαλαιουχικη', 'ομορρυθμη', 'κατα', 'συμπλοιοκτησια', 'ανωνυμη', 'etaireia', 'periorismenis', 'evropaiki', 'metoches', 'idiotiki', 'naftiki', 'eteria', 'eterorithmi', 'euthinis', 'astiki', 'proswpiki', 'sinetairismos', 'lipa', 'prosopa', 'dikeou', 'dimosiou', 'nomika', 'afanis', 'kinopraxia', 'kefaleouhiki', 'somatia', 'idrimata', 'omorithmi', 'kata', 'eterorrythmi', 'simplioktisia', 'anonimi', 'ltd', 'lp', 'unltd', 'ultd', '有限公司', '無限公司', 'partnership', 'limited', 'by', 'group', 'public', 'company', 'guarantee', 'unlimited', 'shares', 'private', 'non', 'share', 'registered', 'entity', 'capital', 'trustee', 'ordinance', 'established', 'kong', 'hong', 'with', '私人股份有限公司', '註冊受託人', '根據法例成立的實體', '公眾股份有限公司', '非香港公司', '有股本的公眾無限公司', '擔保有限公司', '有股本的私人無限公司', '有限責任合夥', 'gu', 'si', 'fen', 'gong', 'xian', 'ren', 'you', 'ce', 'tuo', 'zhu', 'shou', 'fa', 'yan', 'cheng', 'li', 'ju', 'shi', 'de', 'gen', 'zhong', 'gang', 'fei', 'xiang', 'ben', 'wu', 'dan', 'bao', 'ze', 'huo', 'he', 'sce', 'se', 'giu', 'egiu', 'tp', 'jtd', 'dd', 'kd', 'jdoo', 'doo', 'sce', 'se', 'europaea', 'societas', 'kreditna', 'unija', 'interesno', 'gospodarsko', 'udruzenje', 'skraceno', 'europsko', 'egiu', 'zadruga', 'cooperativa', 'europska', 'trgovac', 'pojedinac', 'drustvo', 'masa', 'stecajna', 'zadruge', 'savez', 'trgovacko', 'javno', 'dionicko', 'komanditno', 'podruznica', 'group', 's', 'odgovornoscu', 'jednostavno', 'ogranicenom', 'zajednica', 'ustanova', 's', 'odgovornoscu', 'drustvo', 'ogranicenom', 'se', 'nyrt', 'zrt', 'rt', 'kht', 'kkt', 'kft', 'bt', 'kbe', 'hsz', 'tksz', 'oba', 'koztestulet', 'egyeb', 'egyesulet', 'reszvenytarsasag', 'mukodo', 'nyilvanosan', 'befektetesi', 'alap', 'magannyugdijpenztar', 'zartkoruen', 'alapitvany', 'kolcsonos', 'biztosito', 'szovetkezet', 'tarsasag', 'kozhasznu', 'kozkereseti', 'onkentes', 'biztositopenztar', 'vallalkozas', 'kepviselete', 'kereskedelmi', 'kulfoldi', 'szekhelyu', 'korlatolt', 'felelossegu', 'beteti', 'szemelyisegu', 'nem', 'sorolt', 'jogi', 'mashova', 'szovetseg', 'kiveve', 'sportszovetseg', 'fioktelepe', 'hitelszovetkezet', 'takarek', 'es', 'europai', 'orszagos', 'betetbiztositasi', 'limited', 'ltd', 'ilp', 'se', 'by', 'guarantee', 'ulc', 'eeig', 'plc', 'icav', 'dac', '–', 'clg', 'uc', 'pulc', 'shares', 'puc', 'i&ps', 'group', 'cga', 'ctr', 'cn', 'teo', 'cti', 'cpt', 'partnership', 'limited', 'by', 'public', 'company', 'guarantee', 'no', 'unlimited', 'shares', 'europaea', 'societas', 'private', 'union', 'society', 'general', 'share', 'capital', 'investment', 'interest', 'collective', 'economic', 'european', 'irish', 'vehicle', 'asset', 'management', 'grouping', 'friendly', 'designated', 'dac', 'activity', '–', 'that', 'has', 'ltd', 'provident', 'industrial', 'ainmnithe', 'ghniomhaiochta', 'cuideachta', 'theorainn', 'rathaiochta', 'faoi', 'neamhtheoranta', 'teoranta', 'infheistiochta', 'comhphairtiocht', 'theoranta', 'phoibli', 'partnership', 'limited', 'by', 'public', 'company', 'guarantee', 'liability', 'unlimited', 'shares', 'private', 'society', 'act', 'share', 'capital', 'without', 'not', 'foundation', 'with', 'industrial', 'having', '1931', 'group', '2006', 'personality', 'legal', 'building', 'se', 'slhf', 'slf', 'hf', 'ehf', 'samlagshlutafelag', 'samlagsfelag', 'evropufelag', 'hlutafelag', 'einkahlutafelag', 'co', 'se', 'sc', 'so', 'sp', 'ss', 'el', 'ed', 'ge', 'fi', 'rs', 'sg', 'sl', 'cf', 'at', 'rc', 'll', 'ei', 'di', 'oc', 'sr', 'sn', 'sm', 'cm', 'sd', 'ma', 'cz', 'ep', 'sv', 'in', 'sociale', 'speciale', 'municipale', 'cooperativa', 'a', 'altro', 'stato', 'leggi', 'base', 'di', 'societa', 'costituita', 'ente', 'semplice', 'pubblico', 'diritto', 'europeo', 'gruppo', 'economico', 'interesse', 'impresa', 'fondazione', 'responsabilita', 'semplificata', 'limitata', 'europea', 'consortile', 'fidi', 'consorzio', 'group', 'autonoma', 'statale', 'azienda', 'rete', 'giuridica', 'contratto', 'dotato', 'soggettivita', 'dlgs', 'al', '267', '2000', 'cui', 'individuale', 'azioni', 'per', 'nome', 'collettivo', 'mutuo', 'soccorso', 'mutua', 'assicurazione', 'alla', 'professionisti', 'tra', 'altro', 'a', 'stato', 'leggi', 'base', 'di', 'societa', 'in', 'costituita', 'semplice', 'responsabilita', 'semplificata', 'limitata', 'cooperativa', 'europea', 'consortile', 'azioni', 'per', 'collettivo', 'nome', 'soccorso', 'mutuo', 'professionisti', 'tra', 'ltd', 'inc', 'lp', 'ilp', 'llp', 'p', 'plc', 'slp', 'l', 'arl', 'incorporated', 'partnership', 'limited', 'by', 'public', 'company', 'guarantee', 'liability', 'private', 'partnerships', 'foundation', 'separate', 'sce', 'gesmbh', 'gmbh', 'ag', 'se', 'kg', 'ewiv', 'trust', 'ev', 'eg', 'reg', 'egen', 'genossenschaft', 'europaische', 'mit', 'haftung', 'gesellschaft', 'beschrankter', 'interessenvereinigung', 'wirtschaftliche', 'aktiengesellschaft', 'kommanditgesellschaft', 'stiftung', 'verein', 'treuunternehmen', 'kollektivgesellschaft', 'anstalt', 's', 'a', 'eeig', 'sd', 'ps', 'eb', 'vi', 'ekb', 'apb', 'ab', 'rb', 'ii', 'uab', 'tub', 'lpra', 'tr', 'lf', 'bn', 'bi', 'vs', 'ko', 'kb', 'pdb', 'per', 'etbg', 'crc', 'mb', 'zub', 'cb', 'pp', 'si', 'ar', 'europos', 'bendroves', 'valstybes', 'imones', 'kooperatines', 'bendrijos', 'advokatu', 'profesines', 'seimynos', 'ir', 'susivienijimai', 'sajungos', 'ju', 'akcines', 'centrai', 'bendruomenes', 'religines', 'individualios', 'ekonominiu', 'interesu', 'grupes', 'uzdarosios', 'ukines', 'tikrosios', 'rumu', 'lietuvos', 'prekybos', 'asociacija', 'pramones', 'amatu', 'tradicines', 'asociacijos', 'labdaros', 'fondai', 'paramos', 'istaigos', 'biudzetines', 'viesosios', 'kooperatyvai', 'komanditines', 'detektyvu', 'privaciu', 'rumai', 'institucijos', 'nuolatines', 'arbitrazo', 'sodininku', 'bendradarbiavimo', 'teritorinio', 'pranesimu', 'centras', 'valdymo', 'bendras', 'mazosios', 'zemes', 'ukio', 'centrinis', 'bankas', 'politines', 'partijos', 'savivaldybiu', 'asbl', 'gie', 'sc', 'sa', 'senc', 'ei', 'ep', 'assep', 'am', 'secs', 'aa', 'seca', 'sepcav', 'sicaf', 'aam', 'sarl', 'oth', 'sci', 'secsp', 'sicav', 'fon', '1', 'association', 'public', 'commandite', 'actions', 'societe', 'cooperative', 'responsabilite', 'limitee', 'europeenne', 'entreprise', 'economique', 'groupement', 'interet', 'lucratif', 'but', 'sans', 'nom', 'collectif', 'civile', 'simple', 'etablissement', 'anonyme', 'agricole', 'fondation', 'pension', 'capital', 'commerce', 'loi', 'speciale', 'concernant', 'assurances', 'epargne', 'personnes', 'registre', 'investissement', 'variable', 'individuelle', 'momentanee', 'fixe', 'mutuelles', 'entreprises', '19', 'autres', 'societesdes', '2002', 'morales', 'dont', 'immatriculation', 'modifiee', 'article', 'est', 'prevue', 'decembre', 'societe', 'europeenne', 'se', 'as', 'ks', 'ps', 'ik', 'sia', 'komanditsabiedriba', 'pilnsabiedriba', 'komercsabiedriba', 'eiropas', 'komersants', 'individualais', 'ierobezotu', 'ar', 'atbildibu', 'sabiedriba', 'akciju', 'tp', 'jtd', 'kd', 'doo', 'kda', 'ad', 'siz', 'акции', 'ограничена', 'со', 'друштво', 'командитно', 'акционерско', 'трговско', 'претпријатие', 'јавно', 'интересна', 'заедница', 'стопанска', 'одговрност', 'подрушница', 'на', 'односно', 'странски', 'странско', 'трговрец', 'поединец', 'трговец', 'komanditno', 'drustvo', 'akcii', 'so', 'akcionersko', 'javno', 'trgovsko', 'pretprijatie', 'zaednica', 'interesna', 'stopanska', 'ogranicena', 'odgvornost', 'na', 'odnosno', 'trgovec', 'poedinec', 'stransko', 'stranski', 'podruznica', 'limited', 'ltd', 'lp', 'se', 'partnership', 'eeig', 'plc', 'partnership', 'limited', 'public', 'company', 'liability', 'europaea', 'societas', 'in', 'nom', 'collectif', 'private', 'interest', 'economic', 'european', 'grouping', 'limitata', 'commendite', 'en', 'akkomandita', 'jew', 'socjeta', 'pubblika', 'kumpanija', 'kollettiv', 'f', 'isem', 'privata', 'coop', 'ltd', 'lp', 'llp', 'pc', 'ltee', 'societe', 'tu', 'plc', 'pt', 'f', 'ste', 'business', 'limited', 'by', 'public', 'company', 'guarantee', 'liability', 'shares', 'societe', 'private', 'companies', 'trade', 'unions', 'partnerships', 'cooperatives', 'associations', 'foundations', 'companiy', 'bodies', 'parastal', 'ministries', 'others', 'companies', 'limited', 'by', 'private', 'guarantee', 'public', 'vof', 'bv', 'nv', 'coop', 'sce', 'se', 'eesv', 'cv', 'owm', 'io', 'rp', 'vve', 'cooperatie', 'stichting', 'vennootschap', 'onder', 'firma', 'commanditaire', 'besloten', 'vereniging', 'naamloze', 'eenmanszaak', 'maatschap', 'beperkte', 'met', 'aansprakelijkheid', 'europaea', 'societas', 'in', 'europese', 'europees', 'economisch', 'samenwerkingsverband', 'van', 'fonds', 'cooperatie', 'cooperativa', 'rederij', 'onderlinge', 'waarborgmaatschappij', 'rechtspersoon', 'publiekrechtelijke', 'oprichting', 'eigenaars', 'gemene', 'voor', 'rekening', 'kerkgenootschap', 'sce', 'se', 'sa', 'eøfg', 'as', 'ks', 'ans', 'kf', 'nuf', 'sf', 'fkf', 'bbl', 'da', 'enk', 'asa', 'brl', 'ba', 'iks', 'person', 'med', 'ansvar', 'økonomisk', 'forening', 'selskap', 'ansvarlig', 'stiftelse', 'foretak', 'kommunalt', 'norskregistrert', 'utenlandsk', 'statsforetak', 'fylkeskommunalt', 'gjensidig', 'forsikringsselskap', 'boligbyggelag', 'partsrederi', 'pensjonskasse', 'delt', 'foretaksgruppe', 'europeisk', 'enkeltpersonforetak', 'forening?', 'innretning', 'bare', 'eller', 'lag', 'juridisk', 'annen', 'allmennaksjeselskap', 'samvirkeforetak', 'verdipapirfond', 'kommandittselskap', 'borettslag', 'konkursbo', 'begrenset', 'sparebank', 'aksjeselskap', 'interkommunalt', 'eierseksjonssameie', 'coop', 'ltd', 'lp', 'ultd', 'partnership', 'limited', 'company', 'liability', 'unlimited', 'cooperative', 'ltd', 'llp', 'guarantee', 'pvt', 'smc', 'unlimited', 'association', 'partnership', 'limited', 'by', 'public', 'company', 'guarantee', 'liability', 'unlimited', 'private', 'profit', 'share', 'member', 'capital', 'without', 'not', 'for', 'having', 'multi', 'single', 'unlisted', 'listed', 'se', 'sc', 'sa', 'sp', 'spp', 'sj', 'spk', 'oo', 'z', 'ska', 'ofe', 'tuw', 'partie', 'osoby', 'samodzielne', 'opieki', 'zakłady', 'publiczne', 'zdrowotnej', 'społki', 'partnerskie', 'izby', 'cechy', 'rzemieslnicze', 'i', 'gospodarcze', 'administracji', 'kontroli', 'oraz', 'prawa', 'trybunały', 'ochrony', 'rzadowej', 'organy', 'panstwowej', 'sady', 'władzy', 'jawne', 'zagranicznego', 'oddział', 'reasekuracji', 'zakładu', 'głowny', 'zrzeszenia', 'społdzielnie', 'fundacje', 'samorzadowe', 'organizacyjne', 'jednostki', 'komandytowe', 'gospodarki', 'budzetowej', 'instytucje', 'wzajemnej', 'towarzystwa', 'panstwa', 'skarb', 'rolnicze', 'kołka', 'akcyjne', 'zawodowe', 'społeczne', 'organizacje', 'mieszkaniowe', 'wspolnoty', 'społdzielcze', 'kasy', 'kredytowe', 'oszczednosciowo', 'polityczne', 'społka', 'europejska', 'panstwowe', 'badawcze', 'instytuty', 'zwiazki', 'odpowiedzialnoscia', 'ograniczona', 'z', 'komandytowo', 'ubezpieczen', 'fundusze', 'emerytalne', 'otwarte', 'systemu', 'placowki', 'oswiaty', 'inwestycyjne', 'przedsiebiorcy', 'przedsiebiorstwa', 'koscioły', 'wyznaniowe', 'inne', 'niz', 'wzajemnych', 'uczelnie', 'cywilne', 'działalnosc', 'prowadzace', 'fizyczne', 'gospodarcza', 'stowarzyszen', 'stowarzyszenia', 'trust', 'cooperativa', 'municipal', 'economico', 'interesse', 'nome', 'financeira', 'exterior', 'sucursal', 'de', '2o', 'grau', 'permanente', 'representacao', 'intermunicipal', 'entidade', 'empresarial', 'fundo', 'europeu', 'agrupamento', 'publica', 'associacao', 'anonima', 'sociedade', 'empresa', 'organismo', 'administracao', 'da', 'europeia', 'em', 'coletivo', 'metropolitana', 'comandita', 'publico', 'coletiva', 'direito', 'pessoa', 'internacional', 'por', 'quotas', 'unipessoal', 'desportiva', 'complementar', 'empresas', 'fundacao', 'responsabilidade', 'limitada', 'estabelecimento', 'individual', 'regional', 'sce', 'se', 'sca', 'geie', 'snc', 'gie', 'scs', 'sa', 'srl', 'ii', 'ong', 'pfi', 'ra', 'pfa', 'af', 'in', 'forme', 'non', 'cooperativa', 'regie', 'centrale', 'economic', 'european', 'limitata', 'autonoma', 'de', 'comandita', 'societate', 'europeana', 'mestesugareasca', 'interes', 'grupul', 'organizatie', 'guvernamentala', 'ale', 'si', 'casele', 'organizatii', 'cooperatiste', 'acestora', 'reprezentanta', 'consum', 'fizica', 'independenta', 'persoana', 'pe', 'actiuni', 'proprietate', 'alte', 'intreprindere', 'individuala', 'agricola', 'nume', 'colectiv', 'autorizata', 'sucursala', 'reprezentant', 'fiscal', 'familiala', 'asociatie', 'simpla', 'raspundere', 'cu', 'кд', 'ад', 'дп', 'пр', 'јп', 'доо', 'од', 'kd', 'ad', 'dp', 'pr', 'jp', 'doo', 'od', 'друштво', 'командитно', 'јавно', 'савез', 'задружни', 'друштвено', 'предузеће', 'предузетник', 'задруга', 'одговорношћу', 'ограниченом', 'са', 'акционарско', 'ортачко', 'komanditno', 'odgovornoscu', 'drustvo', 'ogranicenom', 'javno', 'zadruzni', 'savez', 'preduzece', 'drustveno', 'preduzetnik', 'zadruga', 'sa', 'akcionarsko', 'ortacko', 'с', 'и', 'на', 'ассоциации', 'объединения', 'организации', 'благотворительных', 'союзы', 'общества', 'ответственностью', 'ограниченнои', 'фермерские', 'крестьянские', 'хозяиства', 'автономные', 'некоммерческие', 'учреждения', 'благотворительные', 'общественных', 'объединении', 'кооперативов', 'муниципальные', 'собственников', 'жилья', 'товарищества', 'казенные', 'федеральные', 'предприятия', 'кооперативы', 'сельскохозяиственные', 'производственные', 'кроме', 'сельскохозяиственных', 'производственных', 'профсоюзные', 'коммерческими', 'лица', 'организациями', 'являющиеся', 'прочие', 'юридические', 'россиискои', 'субъектом', 'федерации', 'созданные', 'акционерные', 'публичные', 'адвокаты', 'учредившие', 'адвокатскии', 'кабинет', 'потребительские', 'животноводческие', 'или', 'жилищные', 'жилищно', 'строительные', 'академии', 'государственные', 'наук', 'бюджетные', 'субъектов', 'дачные', 'огороднические', 'садоводческие', 'правовые', 'публично', 'компании', 'образовании', 'муниципальных', 'советы', 'унитарные', 'бюро', 'адвокатские', 'казачьи', 'реестр', 'обществ', 'государственныи', 'казачьих', 'в', 'внесенные', 'кредитные', 'гаражные', 'гаражно', 'для', 'деятельности', 'формы', 'лиц', 'граждан', 'физических', 'организационно', 'некоммерческими', 'являющихся', 'корпоративными', 'юридических', 'огороднических', 'садоводческих', 'некоммерческих', 'дачных', 'партнерства', 'фонды', 'проката', 'экологические', 'общественные', 'корпорации', 'коммерческои', 'артели', 'самоуправления', 'территориальные', 'федерациеи', 'общины', 'малочисленных', 'коренных', 'народов', 'подразделения', 'обособленных', 'структурные', 'подразделении', 'недвижимости', 'второго', 'уровня', 'палаты', 'религиозные', 'обслуживающие', 'перерабатывающие', 'унитарными', 'снабженческие', 'колхозы', 'саморегулируемые', 'вере', 'коммандитные', 'простые', 'без', 'юридического', 'созданных', 'прав', 'непубличные', 'хозяиственные', 'хозяиств', 'главы', 'фермерских', 'крестьянских', 'самодеятельности', 'органы', 'общественнои', 'отделения', 'неправительственных', 'иностранных', 'политические', 'партии', 'сбытовые', 'торговые', 'представительства', 'основанные', 'праве', 'оперативного', 'управления', 'индивидуальные', 'предприниматели', 'экономического', 'взаимодеиствия', 'нотариальные', 'международные', 'межправительственные', 'муниципальным', 'образованием', 'страхования', 'взаимного', 'осуществляющих', 'международных', 'территории', 'деятельность', 'частнои', 'практикои', 'нотариусы', 'занимающиеся', 'хозяиственного', 'ведения', 'работодателеи', 'не', 'к', 'предпринимательству', 'отнесеннои', 'потребительских', 'коллегии', 'адвокатов', 'городские', 'суды', 'межраионные', 'раионные', 'рыболовецкие', 'обособленные', 'филиалы', 'накопительные', 'кредитных', 'неправительственные', 'кооперативные', 'коопхозы', 'общин', 'частные', 'инвестиционные', 'паевые', 'движения', 'негосударственные', 'пенсионные', 'торгово', 'промышленные', 'полные', 's', 'i', 'na', 'assotsiatsii', 'organizatsiy', 'blagotvoritel', 'nykh', 'obyedineniya', 'soyuzy', 'otvetstvennost', 'ogranichennoy', 'yu', 'obshchestva', 'khozyaystva', 'yanskiye', 'krest', 'fermerskiye', 'nekommercheskiye', 'organizatsii', 'avtonomnyye', 'nyye', 'uchrezhdeniya', 'obyedineniy', 'obshchestvennykh', 'kooperativov', 'munitsipal', 'tovarishchestva', 'sobstvennikov', 'zhil', 'ya', 'federal', 'kazennyye', 'predpriyatiya', 'sel', 'kooperativy', 'skokhozyaystvennyye', 'proizvodstvennyye', 'skokhozyaystvennykh', 'proizvodstvennykh', 'krome', 'profsoyuznyye', 'prochiye', 'kommercheskimi', 'yuridicheskiye', 'yavlyayushchiyesya', 'litsa', 'organizatsiyami', 'sozdannyye', 'subyektom', 'federatsii', 'rossiyskoy', 'publichnyye', 'aktsionernyye', 'advokatskiy', 'advokaty', 'kabinet', 'uchredivshiye', 'zhivotnovodcheskiye', 'skiye', 'potrebitel', 'ili', 'zhilishchnyye', 'zhilishchno', 'stroitel', 'nauk', 'akademii', 'gosudarstvennyye', 'byudzhetnyye', 'subyektov', 'ogorodnicheskiye', 'sadovodcheskiye', 'dachnyye', 'kompanii', 'publichno', 'pravovyye', 'sovety', 'obrazovaniy', 'unitarnyye', 'byuro', 'advokatskiye', 'vnesennyye', 'reyestr', 'v', 'kazach', 'ikh', 'gosudarstvennyy', 'obshchestv', 'kreditnyye', 'garazhno', 'garazhnyye', 'grazhdan', 'dlya', 'lits', 'nosti', 'fizicheskikh', 'formy', 'deyatel', 'organizatsionno', 'pravovyyу', 'yuridicheskikh', 'yavlyayushchikhsya', 'korporativnymi', 'dachnykh', 'ogorodnicheskikh', 'nekommercheskikh', 'sadovodcheskikh', 'partnerstva', 'fondy', 'prokata', 'ekologicheskiye', 'obshchestvennyye', 'korporatsii', 'kommercheskoy', 'arteli', 'territorial', 'samoupravleniya', 'federatsiyey', 'malochislennykh', 'narodov', 'obshchiny', 'korennykh', 'podrazdeleniy', 'obosoblennykh', 'strukturnyye', 'podrazdeleniya', 'nedvizhimosti', 'urovnya', 'vtorogo', 'palaty', 'religioznyye', 'obsluzhivayushchiye', 'pererabatyvayushchiye', 'nekommercheskimi', 'unitarnymi', 'snabzhencheskiye', 'kolkhozy', 'samoreguliruyemyye', 'kommanditnyye', 'vere', 'prostyye', 'prav', 'sozdannykh', 'bez', 'yuridicheskogo', 'nepublichnyye', 'khozyaystvennyye', 'khozyaystv', 'yanskikh', 'fermerskikh', 'glavy', 'obshchestvennoy', 'samodeyatel', 'organy', 'inostrannykh', 'stvennykh', 'otdeleniya', 'nepravitel', 'partii', 'politicheskiye', 'sbytovyye', 'torgovyye', 'predstavitel', 'stva', 'upravleniya', 'prave', 'operativnogo', 'osnovannyye', 'predprinimateli', 'individual', 'ekonomicheskogo', 'vzaimodeystviya', 'notarial', 'mezhpravitel', 'mezhdunarodnyye', 'stvennyye', 'obrazovaniyem', 'nym', 'vzaimnogo', 'strakhovaniya', 'territorii', 'mezhdunarodnykh', 'osushchestvlyayushchikh', 'nost', 'zanimayushchiyesya', 'praktikoy', 'notariusy', 'chastnoy', 'khozyaystvennogo', 'vedeniya', 'rabotodateley', 'ne', 'predprinimatel', 'otnesennoy', 'k', 'stvu', 'skikh', 'kollegii', 'advokatov', 'gorodskiye', 'rayonnyye', 'mezhrayonnyye', 'sudy', 'rybolovetskiye', 'obosoblennyye', 'filialy', 'nakopitel', 'kreditnykh', 'koopkhozy', 'kooperativnyye', 'obshchin', 'chastnyye', 'investitsionnyye', 'payevyye', 'dvizheniya', 'negosudarstvennyye', 'pensionnyye', 'promyshlennyye', 'torgovo', 'polnyye', 'sce', 'se', 'i', 'ek', 'eeig', 'ab', 'kb', 'mb', 'sf', 'tsf', 'hb', 'bab', 'for', 'sb', 'fof', 'ofb', 'fab', 'khf', 'egts', 'brf', 'for', 'forening', 'europeisk', 'naringsverksamhet', 'som', 'ideell', 'bedriver', 'trossamfund', 'medlemsbank', 'europabolag', 'europakooperativ', 'sambruksforening', 'handelsbolag', 'bankaktiebolag', 'ekonomisk', 'kommanditbolag', 'sparbank', 'forsakringsforening', 'omsesidigt', 'forsakringsbolag', 'forsakringsaktiebolag', 'kooperativ', 'hyresrattsforening', 'intressegruppering', 'territoriellt', 'samarbete', 'gruppering', 'bostadsrattsforening', 'bostadsforening', 'aktiebolag', 'ltd', 'lp', 'llp', 'pte', 'business', 'partnership', 'limited', 'company', 'liability', 'foreign', 'local', 'branch', 'se', 'dd', 'kd', 'doo', 'dno', 'kdd', 'evropska', 'z', 'komanditna', 'delniska', 'druzba', 'omejeno', 'odgovornostjo', 'neomejeno', 'o', 's', 'so', 'a', 'p', 'ou', 'csd', 'specorgjednotka', 'jednotzelspravuradu', 'zahranicosoba', 'pravnicka', 'spol', 'akc', 'zastuporginych', 'statov', 'ver', 'obch', 'shr', 'rolnik', 'v', 'or', 'zastupzahrpravosoby', 'jedzboru', 'zel', 'ochrany', 'druzstevny', 'podnik', 'pol', 'hn', 'orgjednpolstrany', 'social', 'zdravpoistovna', 'ziv', 'slobpovolanie', 'fo', 'polnohospodardruzstvo', 'jednstatzeltechins', 'zavod', 'poistovne', 'oblast', 'zivnostnik', 'stathosporgriadokr', 'jednoducha', 'akcie', 'na', 'medzinar', 'org', 'zdruz', 'fyzicka', 'orgjednotka', 'zdruzenia', 'zaujorgdruz', 'spolocna', 'rdis', 'ine', 'skoly', 'pracvysokej', 'ucelova', 'zahr', 'obchorg', 'poistovna', 'banka', 'statpenazustav', 'dochodpoist', 'doplnkova', 'osoby', 'zlozka', 'alebo', 'hospzar', 'kom', 'zdruzmedzinarobchodu', 'obec', 'murad', 'mesto', 'odstepny', 'samostatne', 'podnikajuca', 'prisporg', 'orgzlozka', 'pobocka', 'statpenazust', 'jedn', 'prevadzkaren', 'samost', 'pravosob', 'zaujm', 'slpovolanie', 'ziva', 'nbs', 'orgdruzstiev', 'zaujmova', 'svojpomocpolndruzstvo', 'ina', 'orgverejnej', 'spravy', 'oblorgjednotka', 'europzoskupuzemspol', 'neziskorgposkytvseobprospsluzby', 'infstrediska', 'zahrkul', 'r', 'pzo', 'zahrmajuc', 'verejnopravinstitucia', 'europzoskuphospzaujm', 'zdruzfyzosob', 'zaujmove', 'spolocenstva', 'vlastnikov', 'v', 'europska', 's', 'druzstvo', 'strany', 'podnik', 'hospodarske', 'politicke', 'agentura', 'fond', 'zakona', 'verejna', 'akciova', 'jednotka', 'na', 'akcie', 'prispevkova', 'hospodarska', 'fyzicka', 'osoba', 'rucenim', 'do', 'drobna', 'uradu', 'samostatna', 'majetkovou', 'pravnicka', 'a', 'ustav', 'banka', 'komora', 'obchodu', 'obec', 'osoby', 'burza', 'stavovska', 'vysoka', 'skola', 'mestsky', 'kraj', 'mimo', 'bytove', 'odstepny', 'zavod', 'osob', 'pravnickych', 'ucelova', 'zahranicne', 'strana', 'politicka', 'organy', 'systemu', 'organizacie', 'rozpoctove', 'prispevkove', 'organizacna', 'csd', 'specializovana', 'obecny', 'spravneho', 'zeleznicneho', 'rozpoctova', 'organizacia', 'sidlom', 'so', 'zahranicna', 'sr', 'uzemia', 'spolocnost', 'statny', 'oddieli', 'psn', 'komoditna', 'jednym', 'druzstevny', 'zakladatelom', 'sporitelne', 'pobocka', 'urad', 'krajsky', 'vybor', 'narodny', 'zastupitelske', 'inych', 'statov', 'obchodna', 'profesna', 'rolnik', 'hospodariaci', 'obchodnom', 'samostatne', 'registri', 'zapisany', 'nezapisany', 'stredna', 'samospravneho', 'kraja', 'samospravny', 'fondy', 'europske', 'pravnickej', 'zastupenie', 'zahranicnej', 'zboru', 'zeleznic', 'ozbrojenej', 'ochrany', 'polnohospodarsky', 'politickej', 'politickeho', 'hnutia', 'zdravotne', 'socialna', 'poistovne', 'sucasne', 'or', 'ako', 'zapisv', 'samhosprolnik', 'podnikatel', 'podnikajuca', 'slobodne', 'zaklade', 'povolanie', 'ineho', 'zivnostenskeho', 'polnohospodarske', 'neinvesticny', 'zeleznicno', 'inspekcie', 'technickej', 'statnej', 'oblastny', 'statna', 'uradom', 'riadena', 'okresnym', 'jednoducha', 'zakladna', 'zdruzenia', 'medzinarodne', 'bydliskom', 'poistovaci', 'spolok', 'spolocna', 'druzstiev', 'zaujmova', 'cinna', 'danoveho', 'prilezitostne', 'informacneho', 'zapisana', 'skoly', 'pracovisko', 'vysokej', 'fakulty', 'ine', 'zahranicno', 'poistovna', 'cirkevna', 'penazny', 'doplnkova', 'dochodkova', 'vyrobne', 'zlozka', 'podniku', 'zariadenie', 'alebo', 'komanditna', 'zdruzenie', 'medzinarodneho', 'komor', 'vynimkou', 'profesnych', 'fakulta', 'mesto', 'zapisujuca', 'ina', 'obchodneho', 'registra', 'sa', 'pravnou', 'odvodenou', 'prispevkovej', 'subjektivitou', 'statneho', 'ustavu', 'penazneho', 'zakladatelmi', 'spolocny', 'viacerymi', 'sporitelna', 'neurcene', 'zatial', 'nespecifikovana', 'forma', 'pravna', 'spotrebne', 'prevadzkaren', 'obecneho', 'ai', 'zvaz', 'klub', 'sposobilosti', 'miestna', 'bez', 'pravnej', 'zaujmove', 'nezapisv', 'povolanim', 'slobodnym', 'slovenska', 'narodna', 'svojpomocne', 'spravy', 'verejnej', 'zeleznice', 'nadacia', 'oblastna', 'uzemnej', 'spoluprace', 'zoskupenie', 'poskytujuca', 'vseobecne', 'prospesne', 'neziskova', 'sluzby', 'televizna', 'kulturne', 'stredisko', 'tlacova', 'rozhlasova', 'informacne', 'obmedzenym', 'hnutie', 'zahranicneho', 'zahranicnou', 'ucastou', 'verejnopravna', 'institucia', 'hospodarskych', 'zaujmov', 'fyzickych', 'pozemkov', 'vlastnikov', 'pod', 'spolocenstva', 'bytov', 'ltd', 'as', 'kollsti', 'komsti', 'sti', 'limited', 'kollektif', 'sirket', 'komandit', 'anonim', 'operative', 'limited', 'cooperative', 'coop', 'co', 'ltd', 'inc', 'lp', 'liability', 'corporation', 's', 'llp', 'corp', 'pc', 'company', 'partnership', 'incorporated', 'association', 'l', 'pllc', 'electric', 'membership', 'emc', 'l3c', 'ssb', 'registered', 'rllp', 'llc', 'lllp', 'rlllp', 'pll', 'having', 'assn', 'chtd', 'lca', 'assoc', 'lc', 'business', 'corporation', 'association', 'partnership', 'limited', 'public', 'company', 'liability', 'cooperative', 'close', 'sole', 'trust', 'professional', 'loan', 'general', 'non', 'profit', 'agricultural', 'religious', 'mutual', 'insurance', 'registered', 'corporations', 'fair', 'for', 'generation', 'including', 'associations', 'municipal', 'state', 'nonprofit', 'development', 'benefit', 'membership', 'electric', 'marketing', 'transmission', 'firms', 'trusts', 'financial', 'partership', 'producer', 'cemetery', 'investor', 'county', 'railroad', 'savings', 'communit', 'l3c', 'transportation', 'authority', 'captive', 'bank', 'burial', 'statutory', 'series', 'llc', 'operative', 'co', 'incorporated', 'limited', 'public', 'company', 'private', 'trust', 'union', 'society', 'charitable', 'overseas', 'ltd', 'inc', 'pty', 'cc', 'npc', 'soc', 'corporation', 'co', 'public', 'company', 'liability', 'private', 'close', 'non', 'profit', 'operatives', 'external', 'secondary', 'primary', 'state', 'owned', 'personal', 'tertiary']

def levenshtein(str1, str2):
    counter = {"+": 0, "-": 0}
    distance = 0
    for edit_code, *_ in ndiff(str1, str2):
        if edit_code == " ":
            distance += max(counter.values())
            counter = {"+": 0, "-": 0}
        else: 
            counter[edit_code] += 1
    distance += max(counter.values())
    return distance

class MatchingResult:
    def __init__(self, score=0):
        self.score = score


class MatcherMixin:

    def match(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        new_lhs, new_rhs = self.normalize(lhs, rhs, original_lhs, original_rhs, **parameters)
        return self.compare(new_lhs, new_rhs, original_lhs, original_rhs, **parameters), new_lhs, new_rhs

    def compare(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        return None

    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        return lhs, rhs


class ComparerMixin(MatcherMixin):

    def compare(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        return self.compare(lhs, rhs, original_lhs, original_rhs, **parameters), lhs, rhs


class NormalizerMixin(MatcherMixin):

    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        return self.normalize(lhs, rhs, original_lhs, original_rhs, **parameters)


class TokenCategoryComparer(ComparerMixin):
    '''If some abbreviations are remaining'''
    def compare(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        try:
            abbreviations_lhs = lhs[0]
            company_words_lhs = lhs[1]
            abbreviations_rhs = rhs[0]
            company_words_rhs = rhs[1]

            number_of_entity_words = len(abbreviations_lhs) + len(company_words_lhs) + len(abbreviations_rhs) + len(
                                                                                                    company_words_rhs)
        except:
            pass

class OtherWordsComparer(ComparerMixin):

    def compare(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        typographies_in_raw=40
        ratio = fuzz.token_sort_ratio(str(lhs), str(rhs))
        return MatchingResult(ratio)


class LevenshteinComparer(ComparerMixin):

    def compare(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        edit = levenshtein(lhs, rhs)

        if edit <= parameters.get("maximal_typographies_in_raw", 1):
            ratio = self.__ratio_distance(edit, lhs, rhs)
            if edit == 0 and len(lhs) == len(rhs):
                return MatchingResult(ratio)
            else:
                return MatchingResult(ratio)

    def __ratio_distance(self, edit_score, lhs, rhs):
        if edit_score == 0:
            return 100
        else:
            len_sum = len(lhs) + len(rhs)
            return int(((len_sum - edit_score) / len_sum) * 100)


class ElfType(IntEnum):
    '''first column of the elf_company dataset'''
    Abbreviation = 0,
    LocalName = 1, # = company word
    TransliteratedAbbreviation = 2,
    TransliteratedLocalName = 3,
    Unknown = 5


class Elf:
    def __init__(self):
        content = pkg_resources.open_text('company_name_matching2', 'elf_company.csv')
        self.__elf_database = self.__read_from_csv(content)

    def get(self, elf_type, token, country='AA'):
        country_mapping = self.__elf_database[country]
        if country_mapping[elf_type] is None:
            return None
        else:
            return country_mapping[elf_type].get(token)

    def __read_from_csv(self, content):
        elf_database = {}
        spamreader = csv.reader(content, delimiter=',', quotechar='"', strict=True)
        for tokens in spamreader:

            country = tokens[0]
            elf_type = ElfType(int(tokens[1]))
            word = tokens[2]
            elfs = set(tokens[3].split(';'))

            country_mapping = elf_database.get(country, None)
            if country_mapping is None:
                word_mapping = {}
                word_mapping[word] = elfs
                country_mapping = [None for _ in range(4)]
                country_mapping[elf_type] = word_mapping
            else:
                word_mapping = country_mapping[elf_type]
                if word_mapping is not None:
                    word_mapping[word] = elfs
                else:
                    word_mapping = { word: elfs }
                country_mapping[elf_type] = word_mapping

            elf_database[country] = country_mapping
        return elf_database


class UnicodeNormalizer(NormalizerMixin):

    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        normalized_lhs = self.__normalize(lhs)
        normalized_rhs = self.__normalize(rhs)
        return normalized_lhs, normalized_rhs

    def __normalize(self, input_str):
        nfkd_form = unicodedata.normalize('NFKD', input_str.casefold())
        return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


class TokenCategoryNormalizer(NormalizerMixin):

    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        new_lhs = self.__categorize_tokens(lhs, **parameters)
        new_rhs = self.__categorize_tokens(rhs, **parameters)
        return new_lhs, new_rhs

    def __categorize_tokens(self, tokens, **parameters):
        abbreviations = {} # abbreviations: ltd, ...
        company_words = {} # corporation, limited, ...
        others = [] # if no abbreviation and no company words

        elf = parameters["ELF"]
        transliterate_function = parameters.get("transliterate", None)

        for token in tokens:
            category, elfs = self.__categorize_token(token, parameters)
            if category == ElfType.Abbreviation or category == ElfType.TransliteratedAbbreviation:
                abbreviations[token] = elfs
            elif category == ElfType.LocalName or category == ElfType.TransliteratedLocalName:
                company_words[token] = elfs
            else:
                if transliterate_function is not None:
                    transliteration = transliterate_function(token)

            others.append(token)
        return abbreviations, company_words, others

    def __categorize_token(self, token, parameters):

        elf = parameters["ELF"]
        transliterate_function = parameters.get("transliterate", None)

        abbreviations_elfs = elf.get(ElfType.Abbreviation, token)
        local_names_elfs = elf.get(ElfType.LocalName, token)

        if abbreviations_elfs is None and local_names_elfs is None:
            if transliterate_function is None:
                return ElfType.Unknown, None
            
            transliterated_token = transliterate_function(token)
            transliterated_abbreviations_elfs = elf.get(ElfType.TransliteratedAbbreviation, transliterated_token)
            transliterated_local_names_elfs = elf.get(ElfType.TransliteratedLocalName, transliterated_token)
            if transliterated_abbreviations_elfs is None and transliterated_local_names_elfs is None:
                return ElfType.Unknown, None
            elif transliterated_abbreviations_elfs is None and transliterated_local_names_elfs is not None:
                return ElfType.LocalName, transliterated_local_names_elfs
            elif transliterated_abbreviations_elfs is not None and transliterated_local_names_elfs is None:
                return ElfType.Abbreviation, transliterated_abbreviations_elfs
            else:
                if len(transliterated_abbreviations_elfs) > len(transliterated_local_names_elfs):
                    return ElfType.Abbreviation, transliterated_abbreviations_elfs
                else:
                    return ElfType.LocalName, transliterated_local_names_elfs
            
        elif abbreviations_elfs is None and local_names_elfs is not None:
            return ElfType.LocalName, local_names_elfs
        elif abbreviations_elfs is not None and local_names_elfs is None:
            return ElfType.Abbreviation, abbreviations_elfs
        else:
            if len(abbreviations_elfs) > len(local_names_elfs):
                return ElfType.Abbreviation, abbreviations_elfs
            else:
                return ElfType.LocalName, local_names_elfs


class StripNormalizer(NormalizerMixin):

    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        return lhs.strip(), rhs.strip()


class SplitNormalizer(NormalizerMixin):

    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        return lhs.split(), rhs.split()


class OtherWordsAbbreviationNormalizer(NormalizerMixin):

    def __init__(self, abbreviations):
        self.abbreviations = abbreviations

    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        original_length = len(lhs)
        lhs_to_remove = set()
        rhs_to_remove = set()
        considered_lhs = [False for _ in range(len(lhs))]
        considered_rhs = [False for _ in range(len(rhs))]
        for index, l in enumerate(lhs):
            others = self.abbreviations.get(l, None)
            if others is not None:
                for other in others:
                    if other in rhs:
                        pos = rhs.index(other)
                        if pos != -1 and considered_rhs[pos] == False:
                            try:
                                considered_lhs[index] = True
                            except:
                                pass
                            try:
                                considered_rhs[pos] = True
                            except:
                                pass
                            lhs_to_remove.add(l)
                            rhs_to_remove.add(other)

        for index, l in enumerate(rhs):
            if not considered_rhs[index]:
                others = self.abbreviations.get(l, None)
                if others is not None:
                    for other in others:
                        if other in lhs:
                            pos = lhs.index(other)
                            if pos != -1 and considered_lhs[pos] == False:
                                try:
                                    considered_lhs[index] = True
                                except:
                                    pass
                                try:
                                    considered_rhs[pos] = True
                                except:
                                    pass
                                lhs_to_remove.add(l)
                                rhs_to_remove.add(other)

        for to_remove_lhs in lhs_to_remove:
            try:
                lhs.remove(to_remove_lhs)
            except:
                pass
        for to_remove_rhs in rhs_to_remove:
            try:
                rhs.remove(to_remove_rhs)
            except:
                pass
        return lhs, rhs


class MisplacedCharacterNormalizer(NormalizerMixin):

    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        normalized_lhs = self.__normalize(lhs)
        normalized_rhs = self.__normalize(rhs)
        return normalized_lhs, normalized_rhs

    def __normalize(self, input_str):
        final = []
        tokens = input_str.split()
        for token in tokens:
            if '.' in token:
                parts = token.split('.')
                # If there are more than 2 dots, it's likely to be initials.
                if len(parts) == 2:
                    final.append(parts[0])
                    final.append(parts[1])
                else:
                    final.append(token.replace('.', ''))
            elif '&' in token and token != '&':
                parts = token.split('&')
                # If there are more than 2 parts, I don't know what it can be oO.
                if len(parts) == 2:
                    final.append(parts[0])
                    final.append('&')
                    final.append(parts[1])
                else:
                    final.append(token.replace('&', ''))
            else:
                final.append(token)
        return u' '.join(final)



class KeepOtherWordsNormalizer(NormalizerMixin):

    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        normalized_lhs = lhs[2]
        normalized_rhs = rhs[2]
        lhs_all_abrv = lhs[0].copy()
        lhs_all_abrv.update(lhs[1])
        rhs_all_abrv = rhs[0].copy()
        rhs_all_abrv.update(rhs[1])
        for elements_lhs in lhs_all_abrv.values():
            for element_lhs in elements_lhs:
                if element_lhs == "TY0P":
                    lhs_remove = [k for k, v in lhs_all_abrv.items() if element_lhs in v]
                    if len(lhs_remove) > 0:
                        try:
                            normalized_lhs.remove(lhs_remove[0])
                        except:
                            pass
                for elements_rhs in rhs_all_abrv.values():
                    if element_lhs in elements_rhs:
                        lhs_element_lhs_to_remove = [k for k, v in lhs_all_abrv.items() if element_lhs in v]
                        if len(lhs_element_lhs_to_remove) > 0:
                            if lhs_element_lhs_to_remove[0] in normalized_lhs:
                                normalized_lhs.remove(lhs_element_lhs_to_remove[0])
                        rhs_element_lhs_to_remove = [k for k, v in rhs_all_abrv.items() if element_lhs in v]
                        if len(rhs_element_lhs_to_remove) > 0:
                            if rhs_element_lhs_to_remove[0] in normalized_rhs:
                                normalized_rhs.remove(rhs_element_lhs_to_remove[0])
        for elements_rhs in rhs_all_abrv.values():
            for element_rhs in elements_rhs:        
                if element_rhs == "TY0P":
                    rhs_remove = [k for k, v in rhs_all_abrv.items() if element_rhs in v]
                    if len(rhs_remove) > 0:
                        try:
                            normalized_rhs.remove(rhs_remove[0])
                        except:
                            pass
        return normalized_lhs, normalized_rhs


class CommonAbbreviationNormalizer(NormalizerMixin):
    '''delete abbreviaitons with common tags (between the left & right words'''
    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        try:
            abbreviations_lhs = lhs[0]
            abbreviations_rhs = rhs[0]
            abbreviations_lhs_to_remove = []
            abbreviations_rhs_to_remove = []
            considered = [False for _ in range(len(rhs))]
            for abbreviation_lhs, elfs_lhs in abbreviations_lhs.items():
                for index, (abbreviation_rhs, elfs_rhs) in enumerate(abbreviations_rhs.items()):
                    try:
                        if not considered[index]:
                            if len(elfs_lhs.intersection(elfs_rhs)) > 0:
                                abbreviations_lhs_to_remove.append(abbreviation_lhs)
                                abbreviations_rhs_to_remove.append(abbreviation_rhs)
                                considered[index] = True
                                break
                    except:
                        pass
            for abbreviation_to_remove in abbreviations_lhs_to_remove:
                del abbreviations_lhs[abbreviation_to_remove]
            for abbreviation_to_remove in abbreviations_rhs_to_remove:
                del abbreviations_rhs[abbreviation_to_remove]
        except:
            pass
        return lhs, rhs


class CharacterNormalizer(NormalizerMixin):

    def __init__(self, meaningless_characters):
        super()
        self.meaningless_characters = meaningless_characters

    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        normalized_lhs = self.__normalize(lhs)
        normalized_rhs = self.__normalize(rhs)
        return normalized_lhs, normalized_rhs

    def __normalize(self, input_str, **parameters):
        without_dot = parameters.get("meaningless_characters", self.meaningless_characters)
        return self.__remove(input_str, without_dot)


    def __remove(self, input_str, characters):
        for character in characters:
            input_str = input_str.replace(character, '')

        return input_str


class AndNormalizer(NormalizerMixin):

    def __init__(self, and_words):
        self.and_words = and_words

    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        return self.__remove_ands(lhs, rhs)

    def __remove_ands(self, lhs, rhs):
        if not ('&' in lhs or '&' in rhs):
            return lhs, rhs

        if '&' in lhs:
            rhs = list(filter(lambda x: x not in self.and_words, rhs))
            lhs = filter(lambda x: x != '&', lhs)
        if '&' in rhs:
            lhs = filter(lambda x: x not in self.and_words, lhs)
            rhs = filter(lambda x: x != '&', rhs)
        return list(lhs), list(rhs)


class AbbreviationLegalFormNormalizer(NormalizerMixin):
    '''Delete the matches between company words and abbreviations:
    take the (left abbreviations, right company words),
    (left company words, right abbreviations) and look if there is
    an intersection between tags, if association: delete them'''
    def normalize(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        abbreviations_lhs = lhs[0]
        company_words_lhs = lhs[1]
        abbreviations_rhs = rhs[0]
        company_words_rhs = rhs[1]

        original_length = len(abbreviations_lhs) + len(company_words_rhs) + len(abbreviations_rhs) + len(
                                                                                                    company_words_lhs)
        self.__remove_abbreviations_of_company_words(abbreviations_lhs, company_words_rhs)
        self.__remove_abbreviations_of_company_words(abbreviations_rhs, company_words_lhs)

        remaining_length = len(abbreviations_lhs) + len(company_words_rhs) + len(abbreviations_rhs) + len(
                                                                                                    company_words_lhs)
        return lhs, rhs

    def __remove_abbreviations_of_company_words(self, abbreviations, company_words):
        abbreviations_to_remove = set()
        company_words_to_remove = set()
        considered = [False for _ in range(len(company_words))]
        for abbreviation, abbreviation_elfs in abbreviations.items():
            for index, (company_word, company_elfs) in enumerate(company_words.items()):
                if not considered[index]:
                    if len(abbreviation_elfs.intersection(company_elfs)) > 0:
                        abbreviations_to_remove.add(abbreviation)
                        company_words_to_remove.add(company_word)
                        considered[index] = True

        for abbreviation_to_remove in abbreviations_to_remove:
            del abbreviations[abbreviation_to_remove]
        for company_word_to_remove in company_words_to_remove:
            del company_words[company_word_to_remove]

        return abbreviations, company_words


class Pipeline:

    def __init__(self, steps):
        self.steps = steps

    def match(self, lhs, rhs, original_lhs, original_rhs, **parameters):
        for i in range(len(self.steps)):
            result, lhs, rhs = self.steps[i].match(lhs, rhs, original_lhs, original_rhs, **parameters)
            if result is not None:
                return result, lhs, rhs

    def __len__(self):
        return len(self.steps)

def make_pipeline(*steps):
    return Pipeline(steps)


class DefaultMatching:   

    def __init__(self, default_parameters=None):
        if default_parameters is None:
            self.default_parameters = MatchingParameters.default()
        else:
            self.default_parameters = default_parameters

        handle_company_words = make_pipeline(
            SplitNormalizer(), # split words
            TokenCategoryNormalizer(), # associate each word to a word from the elf dataset
            #AbbreviationLegalFormNormalizer(), 
            CommonAbbreviationNormalizer(),
            TokenCategoryComparer(),
            KeepOtherWordsNormalizer(), 
            AndNormalizer(self.default_parameters.and_words),
            OtherWordsAbbreviationNormalizer(self.default_parameters.abbreviations),
            OtherWordsComparer()
        )

        self.__pipeline = make_pipeline(
            UnicodeNormalizer(), 
            CharacterNormalizer(self.default_parameters.meaningless_characters_without_dot), 
            MisplacedCharacterNormalizer(),
            handle_company_words
        )

    def match(self, lhs, rhs, **parameters):
        default_parameters = vars(self.default_parameters)
        default_parameters.update(parameters)
        return self.__pipeline.match(lhs, rhs, lhs, rhs, **default_parameters)[0]



class MatchingParameters:
    __MEANINGLESS_CHARACTERS = ['.', ',', '/', '\\', '\'', '(', ')', '’', '-']

    def __init__(self, typographies_in_raw=1, entity_words_unmatched=2, common_words_unmatched=1, maximal_initialism=5, \
                                    remove_common_abbreviations=True, meaningless_characters=__MEANINGLESS_CHARACTERS):
        self.ELF = Elf()
        self.maximal_typographies_in_raw = typographies_in_raw
        self.maximal_entity_words_unmatched = entity_words_unmatched
        self.maximal_common_words_unmatched = common_words_unmatched
        self.maximal_initialism = maximal_initialism
        self.remove_common_abbreviations = remove_common_abbreviations
        self.meaningless_characters = meaningless_characters
        if '.' in meaningless_characters:
            copy = meaningless_characters[:]
            copy.remove('.')
            self.meaningless_characters_without_dot = copy
        else:
            self.meaningless_characters_without_dot = meaningless_characters
        self.transliterate = None
        self.and_words = ['and', 'und', 'et']
        self.abbreviations = json.load(pkg_resources.open_text('company_name_matching2', 'abbreviations.json'))
        #self.abbreviations = json.load(open('data/abbreviations.json'))

    @staticmethod
    def default():
        return MatchingParameters()