import fs from 'fs';

class Journal {
    constructor() {
        this.entries = {}
        this.count  = 0
    }

    addEntry(text) {
        const c = ++this.count;
        const entry = `${c}: ${text}`;
        this.entries[c] = entry
        return c
    }

    removeEntry(index) {
        if (index in this.entries) {
            delete this.entries[index];
            return true;
        }
        return false;
    }

    toString() { // TODO: Remove this persistent behavior from the Journal class
        return Object.values(this.entries).join('\n');
    }

    save() { // TODO: Remove this persistent behavior from the Journal class
        fs.writeFileSync(filename, this.toString());
    }

    load() { // TODO: Remove this persistent behavior from the Journal class
        // return file from local storage
    }

    loadFromUrl(url) { // TODO: Remove this persistent behavior from the Journal class
        // return file from url
    }
}

const journal = new Journal();
journal.addEntry('hi toby');
console.log(' hi: ', journal.toString());
/*
    The problem is that the we're combining persistence management with Journal entry creation/management.

    So if we create a `PersistenceManager` class we can decouple the functionality of Journal creation from Journal management.
*/

class PersistenceManager {
    constructor() {

    }

    preProcess( journal) {
        //
    }

    toString() { // TODO: Remove this persistent behavior from the Journal class
        return Object.values(this.entries).join('\n');
    }

    save() { // TODO: Remove this persistent behavior from the Journal class
        fs.writeFileSync(filename, this.toString());
    }

    load() { // TODO: Remove this persistent behavior from the Journal class
        // return file from local storage
    }

    loadFromUrl(url) { // TODO: Remove this persistent behavior from the Journal class
        // return file from url
    }
}

const p = new PersistenceManager();
const filename = './my-journal';
p.saveToFile(journal, filename);
