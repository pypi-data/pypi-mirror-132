## Hebrew characters

<style type="text/css">
@font-face {
	font-family: "Ezra SIL";
	src: url('https://github.com/annotation/text-fabric/blob/master/tf/server/static/fonts/SILEOT.ttf?raw=true');
	src: url('https://github.com/annotation/text-fabric/blob/master/tf/server/static/fonts/SILEOT.woff?raw=true') format('woff');
}
</style>
<style type="text/css">
body {
    font-family: sans-serif;
}
table.chars {
    border-collapse: collapse;
}
table.chars thead tr {
    color: #ffffff;
    background-color: #444444;
}
table.chars tbody td {
    border: 2px solid #bbbbbb;
    padding: 0.1em 0.5em;
}
h1.chars {
    margin-top: 1em;
}
.t {
    font-family: monospace;
    font-size: large;
    color: #0000ff;
}
.g {
    font-family: "Ezra SIL", sans-serif;
    font-size: x-large;
}
.p {
    font-family: monospace;
    font-size: large;
    color: #666600;
}
.r {
    font-family: sans-serif;
    font-size: small;
    color: #555555;
}
.n {
    font-family: sans-serif;
    color: #990000;
    font-size: small;
}
.u {
    font-family: monospace;
    color: #990000;
}
</style>

!!! note "Disclaimer"
    This just a look-up table, not a full exposition of the organisation of the Masoretic system.

!!! abstract "Transcriptions"
    The ETCBC transcription is used by the ETCBC.
    It has entries for all accents, but not
    for text-critical annotations such as uncertainty, and correction.
    The Abegg transcription is used in the Dead Sea scrolls.
    It has no entries for 
    accents, but it has a repertoire of text-critical marks.
    We have back translated the latter to etcbc-compatible variants
    and entered them in the
    etcbc column, although they are not strictly etcbc marks.

!!! abstract "Phonetics"
    The phonetic representation is meant as a
    tentative 1-1 correspondence with pronunciation, not with the script.
    See
    [phono.ipynb](https://nbviewer.jupyter.org/github/etcbc/phono/blob/master/programs/phono.ipynb),
    where the phonetic transcription is computed and thoroughly documented.

## Consonants

!!! abstract "Details"
    *   For most  consonants: an inner dot is a *dagesh forte*.
    *   For the <span class="g">בגדכפת</span> consonants:
        an inner dot is either a *dagesh forte* or a *dagesh lene*.
    *   When the <span class="g">ה</span> contains a dot, it is called a *mappiq*.

<table class="chars" summary="consonants">
    <thead>
        <tr>
            <th>transcription (etcbc)</th>
            <th>transcription (Abegg)</th>
            <th>glyph</th>
            <th>phonetic</th>
            <th>remarks</th>
            <th>name</th>
            <th>unicode</th>
        </tr>
    </thead>
    <tbody>
<tr>
  <td class="t">&gt;</td>
  <td class="t">a</td>
  <td class="g">א</td>
  <td class="p">ʔ</td>
  <td class="r">when not *mater lectionis*</td>
  <td class="n">*letter* alef</td>
  <td class="u">05D0</td>
</tr>
<tr>
  <td class="t">B</td>
  <td class="t">b</td>
  <td class="g">ב</td>
  <td class="p">bb<br/>b<br/>v</td>
  <td class="r">forte<br/>lene<br/>normal</td>
  <td class="n">*letter* bet</td>
  <td class="u">05D1</td>
</tr>
<tr>
  <td class="t">G</td>
  <td class="t">g</td>
  <td class="g">ג</td>
  <td class="p">gg<br/>g<br/>ḡ</td>
  <td class="r">forte<br/>lene<br/>normal</td>
  <td class="n">*letter* gimel</td>
  <td class="u">05D2</td>
</tr>
<tr>
  <td class="t">D</td>
  <td class="t">d</td>
  <td class="g">ד</td>
  <td class="p">dd<br/>d<br/>ḏ</td>
  <td class="r">forte<br/>lene<br/>normal</td>
  <td class="n">*letter* dalet</td>
  <td class="u">05D3</td>
</tr>
<tr>
  <td class="t">H</td>
  <td class="t">h</td>
  <td class="g">ה</td>
  <td class="p">h</td>
  <td class="r">also with *mappiq*; when not *mater lectionis*</td>
  <td class="n">*letter* he</td>
  <td class="u">05D4</td>
</tr>
<tr>
  <td class="t">W</td>
  <td class="t">w</td>
  <td class="g">ו</td>
  <td class="p">ww<br/>w<br/>û</td>
  <td class="r">forte<br/>when not part of a long vowel<br/>with dagesh as vowel</td>
  <td class="n">*letter* vav</td>
  <td class="u">05D5</td>
</tr>
<tr>
  <td class="t">Z</td>
  <td class="t">z</td>
  <td class="g">ז</td>
  <td class="p">zz<br/>z</td>
  <td class="r">forte<br/>normal</td>
  <td class="n">*letter* zayin</td>
  <td class="u">05D6</td>
</tr>
<tr>
  <td class="t">X</td>
  <td class="t">j</td>
  <td class="g">ח</td>
  <td class="p">ḥ</td>
  <td class="r"></td>
  <td class="n">*letter* het</td>
  <td class="u">05D7</td>
</tr>
<tr>
  <td class="t">V</td>
  <td class="t">f</td>
  <td class="g">ט</td>
  <td class="p">ṭ</td>
  <td class="r"></td>
  <td class="n">*letter* tet</td>
  <td class="u">05D8</td>
</tr>
<tr>
  <td class="t">J</td>
  <td class="t">y</td>
  <td class="g">י</td>
  <td class="p">yy<br/>y<br/>ʸ</td>
  <td class="r">forte<br/>when not part of long vowel<br/>in front of final <span class="g">ו</span></td>
  <td class="n">*letter* yod</td>
  <td class="u">05D9</td>
</tr>
<tr>
  <td class="t">K</td>
  <td class="t">k</td>
  <td class="g">כ</td>
  <td class="p">kk<br/>k<br/>ḵ</td>
  <td class="r">forte<br/>lene<br/>normal</td>
  <td class="n">*letter* kaf</td>
  <td class="u">05DB</td>
</tr>
<tr>
  <td class="t">k</td>
  <td class="t">K</td>
  <td class="g">ך</td>
  <td class="p">k<br/>ḵ</td>
  <td class="r">forte<br/>normal</td>
  <td class="n">*letter* final kaf</td>
  <td class="u">05DA</td>
</tr>
<tr>
  <td class="t">L</td>
  <td class="t">l</td>
  <td class="g">ל</td>
  <td class="p">ll<br/>l</td>
  <td class="r">forte<br/>normal</td>
  <td class="n">*letter* lamed</td>
  <td class="u">05DC</td>
</tr>
<tr>
  <td class="t">M</td>
  <td class="t">m</td>
  <td class="g">מ</td>
  <td class="p">mm<br/>m</td>
  <td class="r">forte<br/>normal</td>
  <td class="n">*letter* mem</td>
  <td class="u">05DE</td>
</tr>
<tr>
  <td class="t">m</td>
  <td class="t">M</td>
  <td class="g">ם</td>
  <td class="p">m</td>
  <td class="r"></td>
  <td class="n">*letter* final mem</td>
  <td class="u">05DD</td>
</tr>
<tr>
  <td class="t">N</td>
  <td class="t">n</td>
  <td class="g">נ</td>
  <td class="p">nn<br/>n</td>
  <td class="r">forte<br/>normal</td>
  <td class="n">*letter* nun</td>
  <td class="u">05E0</td>
</tr>
<tr>
  <td class="t">n</td>
  <td class="t">N</td>
  <td class="g">ן</td>
  <td class="p">n</td>
  <td class="r"></td>
  <td class="n">*letter* final nun</td>
  <td class="u">05DF</td>
</tr>
<tr>
  <td class="t">S</td>
  <td class="t">s</td>
  <td class="g">ס</td>
  <td class="p">ss<br/>s</td>
  <td class="r">forte<br/>normal</td>
  <td class="n">*letter* samekh</td>
  <td class="u">05E1</td>
</tr>
<tr>
  <td class="t">&lt;</td>
  <td class="t">o</td>
  <td class="g">ע</td>
  <td class="p">ʕ</td>
  <td class="r"></td>
  <td class="n">*letter* ayin</td>
  <td class="u">05E2</td>
</tr>
<tr>
  <td class="t">P</td>
  <td class="t">p</td>
  <td class="g">פ</td>
  <td class="p">pp<br/>p<br/>f</td>
  <td class="r">forte<br/>lene<br/>normal</td>
  <td class="n">*letter* pe</td>
  <td class="u">05E4</td>
</tr>
<tr>
  <td class="t">p</td>
  <td class="t">P</td>
  <td class="g">ף</td>
  <td class="p">p<br/>f</td>
  <td class="r">forte<br/>normal</td>
  <td class="n">*letter* final pe</td>
  <td class="u">05E3</td>
</tr>
<tr>
  <td class="t">Y</td>
  <td class="t">x</td>
  <td class="g">צ</td>
  <td class="p">ṣṣ<br/>ṣ</td>
  <td class="r">forte<br/>normal</td>
  <td class="n">*letter* tsadi</td>
  <td class="u">05E6</td>
</tr>
<tr>
  <td class="t">y</td>
  <td class="t">X</td>
  <td class="g">ץ</td>
  <td class="p">ṣ</td>
  <td class="r"></td>
  <td class="n">*letter* final tsadi</td>
  <td class="u">05E5</td>
</tr>
<tr>
  <td class="t">Q</td>
  <td class="t">q</td>
  <td class="g">ק</td>
  <td class="p">qq<br/>q</td>
  <td class="r">forte<br/>normal</td>
  <td class="n">*letter* qof</td>
  <td class="u">05E7</td>
</tr>
<tr>
  <td class="t">R</td>
  <td class="t">r</td>
  <td class="g">ר</td>
  <td class="p">rr<br/>r</td>
  <td class="r">forte<br/>normal</td>
  <td class="n">*letter* resh</td>
  <td class="u">05E8</td>
</tr>
<tr>
  <td class="t">#</td>
  <td class="t">C</td>
  <td class="g">ש</td>
  <td class="p">ŝ</td>
  <td class="r"></td>
  <td class="n">*letter* shin without dot</td>
  <td class="u">05E9</td>
</tr>
<tr>
  <td class="t">C</td>
  <td class="t">v</td>
  <td class="g">שׁ</td>
  <td class="p">šš<br/>š</td>
  <td class="r">forte<br/>normal</td>
  <td class="n">*letter* shin with shin dot</td>
  <td class="u">FB2A</td>
</tr>
<tr>
  <td class="t">F</td>
  <td class="t">c</td>
  <td class="g">שׂ</td>
  <td class="p">śś<br/>ś</td>
  <td class="r">forte<br/>normal</td>
  <td class="n">*letter* shin with sin dot</td>
  <td class="u">FB2B</td>
</tr>
<tr>
  <td class="t">T</td>
  <td class="t">t</td>
  <td class="g">ת</td>
  <td class="p">tt<br/>t<br/>ṯ</td>
  <td class="r">forte<br/>lene<br/>normal</td>
  <td class="n">*letter* tav</td>
  <td class="u">05EA</td>
</tr>
    </tbody>
</table>

## Vowels

!!! caution "Qere Ketiv"
    The phonetics follows the *qere*, not the *ketiv*,
    when they are different.
    In that case a `*` is added.

!!! caution "Tetragrammaton"
    The tetragrammaton <span class="g">יהוה</span>
    is (vowel)-pointed in different ways;
    the phonetics follows the pointing, but the tetragrammaton
    is put between `[ ]`.

<table class="chars" summary="vowels">
    <thead>
        <tr>
            <th>transcription (etcbc)</th>
            <th>transcription (Abegg)</th>
            <th>glyph</th>
            <th>phonetic</th>
            <th>remarks</th>
            <th>name</th>
            <th>unicode</th>
        </tr>
    </thead>
    <tbody>
<tr>
  <td class="t">A</td>
  <td class="t">A Å</td>
  <td class="g"> ַ</td>
  <td class="p">a<br/>ₐ</td>
  <td class="r">normal<br/>*furtive*</td>
  <td class="n">*point* patah</td>
  <td class="u">05B7</td>
</tr>
<tr>
  <td class="t">:A</td>
  <td class="t">S</td>
  <td class="g"> ֲ</td>
  <td class="p">ᵃ</td>
  <td class="r"></td>
  <td class="n">*point* hataf patah</td>
  <td class="u">05B2</td>
</tr>
<tr>
  <td class="t">@</td>
  <td class="t">D ∂ Î</td>
  <td class="g"> ָ</td>
  <td class="p">ā<br/>o</td>
  <td class="r">gadol<br/>qatan</td>
  <td class="n">*point* qamats</td>
  <td class="u">05B8</td>
</tr>
<tr>
  <td class="t">:@</td>
  <td class="t">F ƒ Ï</td>
  <td class="g"> ֳ</td>
  <td class="p">ᵒ</td>
  <td class="r"></td>
  <td class="n">*point* hataf qamats</td>
  <td class="u">05B3</td>
</tr>
<tr>
  <td class="t">E</td>
  <td class="t">R ® ‰</td>
  <td class="g"> ֶ</td>
  <td class="p">e<br/>eʸ</td>
  <td class="r">normal<br/>with following <span class="g">י</span></td>
  <td class="n">*point* segol</td>
  <td class="u">05B6</td>
</tr>
<tr>
  <td class="t">:E</td>
  <td class="t">T</td>
  <td class="g"> ֱ</td>
  <td class="p">ᵉ<br/>ᵉʸ</td>
  <td class="r">normal<br/>with following <span class="g">י</span></td>
  <td class="n">*point* hataf segol</td>
  <td class="u">05B1</td>
</tr>
<tr>
  <td class="t">;</td>
  <td class="t">E é ´</td>
  <td class="g"> ֵ</td>
  <td class="p">ê<br/>ē</td>
  <td class="r">with following <span class="g">י</span><br/>alone</td>
  <td class="n">*point* tsere</td>
  <td class="u">05B5</td>
</tr>
<tr>
  <td class="t">I</td>
  <td class="t">I ˆ î Ê</td>
  <td class="g"> ִ</td>
  <td class="p">î<br/>i</td>
  <td class="r">with following <span class="g">י</span><br/>alone</td>
  <td class="n">*point* hiriq</td>
  <td class="u">05B4</td>
</tr>
<tr>
  <td class="t">O</td>
  <td class="t">O ø</td>
  <td class="g"> ֹ</td>
  <td class="p">ô<br/>ō</td>
  <td class="r">with following <span class="g">ו</span><br/>alone</td>
  <td class="n">*point* holam</td>
  <td class="u">05B9</td>
</tr>
<tr>
  <td class="t">U</td>
  <td class="t">U ü ¨</td>
  <td class="g"> ֻ</td>
  <td class="p">u</td>
  <td class="r"></td>
  <td class="n">*point* qubuts</td>
  <td class="u">05BB</td>
</tr>
<tr>
  <td class="t">:</td>
  <td class="t">V √ J ◊</td>
  <td class="g"> ְ</td>
  <td class="p">ᵊ</td>
  <td class="r">left out if silent</td>
  <td class="n">*point* sheva</td>
  <td class="u">05B0</td>
</tr>
    </tbody>
</table>

## Other points and marks

<table class="chars" summary="other points and marks">
    <thead>
        <tr>
            <th>transcription (etcbc)</th>
            <th>transcription (Abegg)</th>
            <th>glyph</th>
            <th>phonetic</th>
            <th>remarks</th>
            <th>name</th>
            <th>unicode</th>
        </tr>
    </thead>
    <tbody>
<tr>
  <td class="t">.</td>
  <td class="t">; … Ú ¥ Ω</td>
  <td class="g"> ּ</td>
  <td class="p"></td>
  <td class="r"></td>
  <td class="n">*point* dagesh or mapiq</td>
  <td class="u">05BC</td>
</tr>
<tr>
  <td class="t">.c</td>
  <td class="t"></td>
  <td class="g"> ׁ</td>
  <td class="p"></td>
  <td class="r"></td>
  <td class="n">*point* shin dot</td>
  <td class="u">05C1</td>
</tr>
<tr>
  <td class="t">.f</td>
  <td class="t"></td>
  <td class="g"> ׂ</td>
  <td class="p"></td>
  <td class="r"></td>
  <td class="n">*point* sin dot</td>
  <td class="u">05C2</td>
</tr>
<tr>
  <td class="t">,</td>
  <td class="t"></td>
  <td class="g"> ֿ</td>
  <td class="p"></td>
  <td class="r"></td>
  <td class="n">*point* rafe</td>
  <td class="u">05BF</td>
</tr>
<tr>
  <td class="t">35</td>
  <td class="t"></td>
  <td class="g"> ֽ</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*point* meteg</td>
  <td class="u">05BD</td>
</tr>
<tr>
  <td class="t">45</td>
  <td class="t"></td>
  <td class="g"> ֽ</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*point* meteg</td>
  <td class="u">05BD</td>
</tr>
<tr>
  <td class="t">75</td>
  <td class="t"></td>
  <td class="g"> ֽ</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*point* meteg</td>
  <td class="u">05BD</td>
</tr>
<tr>
  <td class="t">95</td>
  <td class="t"></td>
  <td class="g"> ֽ</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*point* meteg</td>
  <td class="u">05BD</td>
</tr>
<tr>
  <td class="t">52</td>
  <td class="t"></td>
  <td class="g"> ׄ</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*mark* upper dot</td>
  <td class="u">05C4</td>
</tr>
<tr>
  <td class="t">53</td>
  <td class="t"></td>
  <td class="g"> ׅ</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*mark* lower dot</td>
  <td class="u">05C5</td>
</tr>
<tr>
  <td class="t">&#42;</td>
  <td class="t"></td>
  <td class="g"> ֯</td>
  <td class="p"></td>
  <td class="r"></td>
  <td class="n">*mark* masora circle</td>
  <td class="u">05AF</td>
</tr>
    </tbody>
</table>

## Punctuation

!!! abstract "Details"
    Some specialties in the Masoretic system are not reflected
    in the phonetics:

    *   *setumah*
        <span class="g">ס</span>;
    *   *petuhah*
        <span class="g">ף</span>;
    *   *nun-hafuka*
        <span class="g"> ̇׆</span>.

<table class="chars" summary="punctuation">
    <thead>
        <tr>
            <th>transcription (etcbc)</th>
            <th>transcription (Abegg)</th>
            <th>glyph</th>
            <th>phonetic</th>
            <th>remarks</th>
            <th>name</th>
            <th>unicode</th>
        </tr>
    </thead>
    <tbody>
<tr>
  <td class="t">00</td>
  <td class="t">.</td>
  <td class="g">׃</td>
  <td class="p">.</td>
  <td class="r"></td>
  <td class="n">*punctuation* sof pasuq</td>
  <td class="u">05C3</td>
</tr>
<tr>
  <td class="t">ñ</td>
  <td class="t"></td>
  <td class="g">׆</td>
  <td class="p"></td>
  <td class="r"></td>
  <td class="n">*punctuation* nun hafukha</td>
  <td class="u">05C6</td>
</tr>
<tr>
  <td class="t">&amp;</td>
  <td class="t">-</td>
  <td class="g">־</td>
  <td class="p">-</td>
  <td class="r"></td>
  <td class="n">*punctuation* maqaf</td>
  <td class="u">05BE</td>
</tr>
<tr>
  <td class="t">&#95;</td>
  <td class="t">&nbsp; (non breaking space)</td>
  <td class="g">&nbsp;</td>
  <td class="p"></td>
  <td class="r"></td>
  <td class="n">space</td>
  <td class="u">0020</td>
</tr>
<tr>
  <td class="t">0000</td>
  <td class="t">±</td>
  <td class="g">׃׃</td>
  <td class="p"></td>
  <td class="r">Dead Sea scrolls. We use as Hebrew character a double sof pasuq.</td>
  <td class="n">paleo-divider</td>
  <td class="u">05C3 05C3</td>
</tr>
<tr>
  <td class="t">'</td>
  <td class="t">/</td>
  <td class="g">׳</td>
  <td class="p"></td>
  <td class="r">Dead Sea scrolls. We use as Hebrew character a geresh.</td>
  <td class="n">morpheme-break</td>
  <td class="u">05F3</td>
</tr>
    </tbody>
</table>

## Hybrid

!!! abstract "Details"
    There is a character that is mostly punctuation, but that 
    can also influence the nature of some accents occurring in the word before.
    Such a character is a hybrid between punctuation and accent.
    See also the documentation of the BHSA about
    [cantillation](https://etcbc.github.io/bhsa/cantillation/).

<table class="chars" summary="accents">
    <thead>
        <tr>
            <th>transcription</th>
            <th>glyph</th>
            <th>phonetic</th>
            <th>remarks</th>
            <th>name</th>
            <th>unicode</th>
        </tr>
    </thead>
    <tbody>
<tr>
  <td class="t">05</td>
  <td class="t"></td>
  <td class="g">׀</td>
  <td class="p"></td>
  <td class="r"></td>
  <td class="n">*punctuation* paseq</td>
  <td class="u">05C0</td>
</tr>
    </tbody>
</table>

## Accents

!!! abstract "Details"
    Some accents play a role in deciding whether a schwa is silent or mobile
    and whether a qamets is gadol or qatan.
    In the phonetics those accents appear as `ˈ` or `ˌ`.
    Implied accents are also added.

<table class="chars" summary="accents">
    <thead>
        <tr>
            <th>transcription</th>
            <th>glyph</th>
            <th>phonetic</th>
            <th>remarks</th>
            <th>name</th>
            <th>unicode</th>
        </tr>
    </thead>
    <tbody>
<tr>
  <td class="t">94</td>
  <td class="g"> ֧</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* darga</td>
  <td class="u">05A7</td>
</tr>
<tr>
  <td class="t">13</td>
  <td class="g"> ֭</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* dehi</td>
  <td class="u">05AD</td>
</tr>
<tr>
  <td class="t">92</td>
  <td class="g"> ֑</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* etnahta</td>
  <td class="u">0591</td>
</tr>
<tr>
  <td class="t">61</td>
  <td class="g"> ֜</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* geresh</td>
  <td class="u">059C</td>
</tr>
<tr>
  <td class="t">11</td>
  <td class="g"> ֝</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* geresh muqdam</td>
  <td class="u">059D</td>
</tr>
<tr>
  <td class="t">62</td>
  <td class="g"> ֞</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* gershayim</td>
  <td class="u">059E</td>
</tr>
<tr>
  <td class="t">64</td>
  <td class="g"> ֬</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* iluy</td>
  <td class="u">05AC</td>
</tr>
<tr>
  <td class="t">70</td>
  <td class="g"> ֤</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* mahapakh</td>
  <td class="u">05A4</td>
</tr>
<tr>
  <td class="t">71</td>
  <td class="g"> ֥</td>
  <td class="p">ˌ</td>
  <td class="r"></td>
  <td class="n">*accent* merkha</td>
  <td class="u">05A5</td>
</tr>
<tr>
  <td class="t">72</td>
  <td class="g"> ֦</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* merkha kefula</td>
  <td class="u">05A6</td>
</tr>
<tr>
  <td class="t">74</td>
  <td class="g"> ֣</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* munah</td>
  <td class="u">05A3</td>
</tr>
<tr>
  <td class="t">60</td>
  <td class="g"> ֫</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* ole</td>
  <td class="u">05AB</td>
</tr>
<tr>
  <td class="t">03</td>
  <td class="g"> ֙</td>
  <td class="p"></td>
  <td class="r"></td>
  <td class="n">*accent* pashta</td>
  <td class="u">0599</td>
</tr>
<tr>
  <td class="t">83</td>
  <td class="g"> ֡</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* pazer</td>
  <td class="u">05A1</td>
</tr>
<tr>
  <td class="t">33</td>
  <td class="g"> ֨</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* qadma</td>
  <td class="u">05A8</td>
</tr>
<tr>
  <td class="t">63</td>
  <td class="g"> ֨</td>
  <td class="p">ˌ</td>
  <td class="r"></td>
  <td class="n">*accent* qadma</td>
  <td class="u">05A8</td>
</tr>
<tr>
  <td class="t">84</td>
  <td class="g"> ֟</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* qarney para</td>
  <td class="u">059F</td>
</tr>
<tr>
  <td class="t">81</td>
  <td class="g"> ֗</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* revia</td>
  <td class="u">0597</td>
</tr>
<tr>
  <td class="t">01</td>
  <td class="g"> ֒</td>
  <td class="p"></td>
  <td class="r"></td>
  <td class="n">*accent* segol</td>
  <td class="u">0592</td>
</tr>
<tr>
  <td class="t">65</td>
  <td class="g"> ֓</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* shalshelet</td>
  <td class="u">0593</td>
</tr>
<tr>
  <td class="t">04</td>
  <td class="g"> ֩</td>
  <td class="p"></td>
  <td class="r"></td>
  <td class="n">*accent* telisha qetana</td>
  <td class="u">05A9</td>
</tr>
<tr>
  <td class="t">24</td>
  <td class="g"> ֩</td>
  <td class="p"></td>
  <td class="r"></td>
  <td class="n">*accent* telisha qetana</td>
  <td class="u">05A9</td>
</tr>
<tr>
  <td class="t">14</td>
  <td class="g"> ֠</td>
  <td class="p"></td>
  <td class="r"></td>
  <td class="n">*accent* telisha gedola</td>
  <td class="u">05A0</td>
</tr>
<tr>
  <td class="t">44</td>
  <td class="g"> ֠</td>
  <td class="p"></td>
  <td class="r"></td>
  <td class="n">*accent* telisha gedola</td>
  <td class="u">05A0</td>
</tr>
<tr>
  <td class="t">91</td>
  <td class="g"> ֛</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* tevir</td>
  <td class="u">059B</td>
</tr>
<tr>
  <td class="t">73</td>
  <td class="g"> ֖</td>
  <td class="p">ˌ</td>
  <td class="r"></td>
  <td class="n">*accent* tipeha</td>
  <td class="u">0596</td>
</tr>
<tr>
  <td class="t">93</td>
  <td class="g"> ֪</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* yerah ben yomo</td>
  <td class="u">05AA</td>
</tr>
<tr>
  <td class="t">10</td>
  <td class="g"> ֚</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* yetiv</td>
  <td class="u">059A</td>
</tr>
<tr>
  <td class="t">80</td>
  <td class="g"> ֔</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* zaqef qatan</td>
  <td class="u">0594</td>
</tr>
<tr>
  <td class="t">85</td>
  <td class="g"> ֕</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* zaqef gadol</td>
  <td class="u">0595</td>
</tr>
<tr>
  <td class="t">82</td>
  <td class="g"> ֘</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* zarqa</td>
  <td class="u">0598</td>
</tr>
<tr>
  <td class="t">02</td>
  <td class="g"> ֮</td>
  <td class="p">ˈ</td>
  <td class="r"></td>
  <td class="n">*accent* zinor</td>
  <td class="u">05AE</td>
</tr>
    </tbody>
</table>

## Numerals

!!! abstract "Details"
    These signs occur in the Dead Sea scrolls.
    We represent them with conventional Hebrew characters for numbers
    and use the geresh accent or another accent to mark the letter
    as a numeral.

    The ETCBC codes are obtained by translating back from the unicode.

<table class="chars" summary="numerals">
    <thead>
        <tr>
            <th>transcription (ETCBC)</th>
            <th>transcription (Abegg)</th>
            <th>glyph</th>
            <th>remarks</th>
            <th>name</th>
        </tr>
    </thead>
    <tbody>
<tr>
  <td class="t">&gt;'</td>
  <td class="t">A</td>
  <td class="g">א֜</td>
  <td class="r"></td>
  <td class="n">*number* 1</td>
</tr>
<tr>
  <td class="t">&gt;52</td>
  <td class="t">å</td>
  <td class="g">אׄ</td>
  <td class="r">alternative for 1, often at the end of a number,
  we use the upper dot to distinguish it from the other 1</td>
  <td class="n">*number* 1</td>
</tr>
<tr>
  <td class="t">&gt;53</td>
  <td class="t">B</td>
  <td class="g">אׅ</td>
  <td class="r">alternative for 1, often at the end of a number,
  we use the lower dot to distinguish it from the other 1</td>
  <td class="n">*number* 1</td>
</tr>
<tr>
  <td class="t">&gt;35</td>
  <td class="t">∫</td>
  <td class="g">אֽ</td>
  <td class="r">alternative for 1, often at the end of a number,
  we use the meteg to distinguish it from the other 1</td>
  <td class="n">*number* 1</td>
</tr>
<tr>
  <td class="t">J'</td>
  <td class="t">C</td>
  <td class="g">י֜</td>
  <td class="r"></td>
  <td class="n">*number* 10</td>
</tr>
<tr>
  <td class="t">k'</td>
  <td class="t">D</td>
  <td class="g">ך֜</td>
  <td class="r"></td>
  <td class="n">*number* 20</td>
</tr>
<tr>
  <td class="t">Q'</td>
  <td class="t">F</td>
  <td class="g">ק֜</td>
  <td class="r"></td>
  <td class="n">*number* 100</td>
</tr>
<tr>
  <td class="t">&amp;</td>
  <td class="t">+</td>
  <td class="g">־</td>
  <td class="r">we use the maqaf to represent addition between numbers</td>
  <td class="n">add</td>
</tr>
    </tbody>
</table>

## Text-critical

!!! abstract "Details"
    These signs occur in the Dead Sea scrolls.
    They are used to indicate uncertainty and editing acts by ancient scribes
    or modern editors.
    They do not have an associated glyph in Unicode.

    The ETCBC does not have codes for them, but we propose an
    ETCBC-compatible encoding for them.
    The ETCBC codes are surrounded by space, except for the brackets,
    where a space at the side of the ( or ) is not necessary.

    Codes that are marked as *flag* apply to the preceding character.

    Codes that are marked as *brackets* apply to the material
    within them.

<table class="chars" summary="text-critical">
    <thead>
        <tr>
            <th>transcription (Abegg)</th>
            <th>transcription (etcbc)</th>
            <th>remarks</th>
            <th>name</th>
        </tr>
    </thead>
    <tbody>
<tr>
  <td class="t">0</td>
  <td class="t">ε</td>
  <td class="r">token</td>
  <td class="n">missing</td>
</tr>
<tr>
  <td class="t">?</td>
  <td class="t"> ? </td>
  <td class="r">token</td>
  <td class="n">uncertain (degree 1)</td>
</tr>
<tr>
  <td class="t">&#92;</td>
  <td class="t"> # </td>
  <td class="r">token</td>
  <td class="n">uncertain (degree 2)</td>
</tr>
<tr>
  <td class="t">�</td>
  <td class="t"> #? </td>
  <td class="r">token</td>
  <td class="n">uncertain (degree 3)</td>
</tr>
<tr>
  <td class="t">Ø</td>
  <td class="t">?</td>
  <td class="r">flag, applies to preceding character</td>
  <td class="n">uncertain (degree 1)</td>
</tr>
<tr>
  <td class="t">«</td>
  <td class="t">#</td>
  <td class="r">flag, applies to preceding character</td>
  <td class="n">uncertain (degree 2)</td>
</tr>
<tr>
  <td class="t">»</td>
  <td class="t">#?</td>
  <td class="r">flag, applies to preceding character</td>
  <td class="n">uncertain (degree 3)</td>
</tr>
<tr>
  <td class="t">&#124;</td>
  <td class="t">##</td>
  <td class="r">flag, applies to preceding character</td>
  <td class="n">uncertain (degree 4)</td>
</tr>
<tr>
  <td class="t">« »</td>
  <td class="t">(# #)</td>
  <td class="r">brackets</td>
  <td class="n">uncertain (degree 2)</td>
</tr>
<tr>
  <td class="t">≤ ≥</td>
  <td class="t">(- -)</td>
  <td class="r">brackets</td>
  <td class="n">vacat (empty space)</td>
</tr>
<tr>
  <td class="t">( )</td>
  <td class="t">( )</td>
  <td class="r">brackets</td>
  <td class="n">alternative</td>
</tr>
<tr>
  <td class="t">[ ]</td>
  <td class="t">[ ]</td>
  <td class="r">brackets</td>
  <td class="n">reconstruction (modern)</td>
</tr>
<tr>
  <td class="t">{ }</td>
  <td class="t">{ }</td>
  <td class="r">brackets</td>
  <td class="n">removed (modern)</td>
</tr>
<tr>
  <td class="t">{&#123; }}</td>
  <td class="t">{&#123; }}</td>
  <td class="r">brackets</td>
  <td class="n">removed (ancient)</td>
</tr>
<tr>
  <td class="t">&lt; &gt;</td>
  <td class="t">(&lt; &gt;)</td>
  <td class="r">brackets</td>
  <td class="n">correction (modern)</td>
</tr>
<tr>
  <td class="t">&lt;&lt; &gt;&gt;</td>
  <td class="t">(&lt;&lt; &gt;&gt;)</td>
  <td class="r">brackets</td>
  <td class="n">correction (ancient)</td>
</tr>
<tr>
  <td class="t">^ ^</td>
  <td class="t">(^ ^)</td>
  <td class="r">brackets</td>
  <td class="n">correction (supralinear, ancient)</td>
</tr>
    </tbody>
</table>
