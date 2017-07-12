//
//  DetailViewController.swift
//  ConsumePython
//
//  Created by David Fekke on 7/10/17.
//  Copyright © 2017 David Fekke. All rights reserved.
//

import UIKit

class DetailViewController: UIViewController {

    @IBOutlet weak var detailDescriptionLabel: UILabel!


    func configureView() {
        // Update the user interface for the detail item.
        let detail = detailItem
        if let label = detailDescriptionLabel {
            label.text = detail
        }
        
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        configureView()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    var detailItem: String = "" {
        didSet {
            // Update the view.
            configureView()
        }
    }


}

